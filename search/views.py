from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
from django.views.generic import ListView
from .filters import PoseFilter
from .models import Pose
from .tables import *
from django.urls import reverse
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

import os
import zipfile
from io import StringIO, BytesIO
# Create your views here.

filepath = '/global/cfs/cdirs/m3718/'

def pose_list(request):
    table = PoseTable(Pose.objects.all())
    return render(request, "search/includes/search_result_test.html", {"table": table})

def filtered_pose_table(request):
    poses = Pose.objects.all()
    my_filter = PoseFilter(request.GET, queryset=poses)
    poses = my_filter.qs
    table = PoseTable(poses)
    RequestConfig(request).configure(table)

    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))

    if request.method == 'POST':
        zip_subdir = "poses"
        zip_filename = "%s.zip" % zip_subdir
        # Open StringIO to grab in-memory ZIP contents
        s = BytesIO()

        # The zip compressor
        zf = zipfile.ZipFile(s, "w")
        for pose in poses:
            fpath = filepath + pose.sdf_file
            # Calculate path for file in zip
            fdir, fname = os.path.split(fpath)
            zip_path = os.path.join(zip_subdir, fname)

            # Add file, at correct path
            zf.write(fpath, zip_path)

        # Must close zip for all contents to be written
        zf.close()

        # Grab ZIP file from in-memory, make response with correct MIME-type
        response = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
        # ..and correct content-disposition
        response['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

        return response

    return render(request, "search/includes/filtered_table.html", {"table": table, 'filter': my_filter})

class PoseListView(ListView):
    model = Pose
    template_name = 'search/includes/search_result_test.html'

def render_download(request, filename):
    #filepath = '/global/cfs/cdirs/m3718/'
    fl = open(filepath + filename, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_test(request):
    #filepath = '/global/cfs/cdirs/m3718/'
    filename = 'SARS_3CLpro_5c5o_ActiveSiteAtomsOnly.pdb'

    fl = open(filepath + filename, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
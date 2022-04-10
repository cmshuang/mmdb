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

filepath = '/global/cfs/cdirs/m3718/OpeNNdd/pose_sdf/' #Hard-coded directory for where all downloadable files are stored.

def filtered_pose_table(request):
    """View for search page"""
    #poses = Pose.objects.all()
    poses = Pose.objects.filter(id__lt=500) #For the sake of demonstration, limit to the first 500 entries
    my_filter = PoseFilter(request.GET, queryset=poses) #Filter poses from form requeset
    poses = my_filter.qs #Get queryset from filter
    table = PoseTable(poses) #Generate table from filtered qs

    #Accept export data request if given, return download response
    RequestConfig(request).configure(table)
    export_format = request.GET.get("_export", None)
    if TableExport.is_valid_format(export_format):
        exporter = TableExport(export_format, table)
        return exporter.response("table.{}".format(export_format))

    #If SDF zip file download button pressed
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

    #Render the html template for display, passing in the table and filter
    return render(request, "search/includes/filtered_table.html", {"table": table, 'filter': my_filter})

def render_download(request, filename):
    """View for file download"""
    fl = open(filepath + filename, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

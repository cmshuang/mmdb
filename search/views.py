from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
from django.views.generic import ListView
from .filters import PoseFilter
from .models import Pose
from .tables import PoseTable
from django.urls import reverse

# Create your views here.

def pose_list(request):
    table = PoseTable(Pose.objects.all())
    return render(request, "search/includes/search_result_test.html", {"table": table})

class PoseListView(ListView):
    model = Pose
    template_name = 'search/includes/search_result_test.html'

def render_download(request, filename):
    filepath = '/global/cfs/cdirs/m3718/'
    fl = open(filepath + filename, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

def download_test(request):
    filepath = '/global/cfs/cdirs/m3718/'
    filename = 'SARS_3CLpro_5c5o_ActiveSiteAtomsOnly.pdb'

    fl = open(filepath + filename, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
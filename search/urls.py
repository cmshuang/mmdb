from django.urls import path

from . import views

urlpatterns = [
    path('download-test/', views.download_test, name='download-test'),
    path('results-test/', views.PoseListView.as_view(), name='results-test'),
    path('tables-test/', views.pose_list, name='tables'),
    path('results/download/<filename>', views.render_download, name='download'),
]
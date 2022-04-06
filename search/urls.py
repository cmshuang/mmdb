from django.urls import path

from . import views

urlpatterns = [
    path('', views.filtered_pose_table, name='home'),
    path('download/<filename>', views.render_download, name='download'),
]
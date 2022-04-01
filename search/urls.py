from django.urls import path

from . import views

urlpatterns = [
    path('filtered-tables-test/', views.filtered_pose_table, name='filtered-tables'),
    path('results/download/<filename>', views.render_download, name='download'),
]
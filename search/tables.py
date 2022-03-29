import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.sites.models import Site
from .filters import PoseFilter
from .models import *

class PoseTable(tables.Table):
    zinc_id = tables.Column(accessor='ligand.zinc_id')
    num_atoms = tables.Column(accessor='ligand.nb_atoms')
    virus_name = tables.Column(accessor='protein.virus_name')
    protein_name = tables.Column(accessor='protein.protein_name')
    sdf_file_link = tables.Column(accessor="sdf_file", linkify=('download', [tables.A('sdf_file')]), empty_values=())
    class Meta:
        model = Pose
        fields = ("binding_affinity",)
        sequence = ('virus_name', 'protein_name', 'zinc_id', 'num_atoms', 'sdf_file_link', 'binding_affinity')

    def value_sdf_file_link(self, record):
        return Site.objects.get_current().domain + reverse('download', kwargs={'filename': record.sdf_file})


class FilteredPoseView(SingleTableMixin, FilterView):
    table_class = PoseTable
    model = Pose
    template_name = "search/includes/filtered_table.html"

    filterset_class = PoseFilter
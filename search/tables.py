import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.sites.models import Site
from .filters import PoseFilter
from .models import *

class PoseTable(tables.Table):
    zinc_id = tables.Column(verbose_name="Ligand ZINC ID", accessor='ligand.zinc_id')
    num_atoms = tables.Column(verbose_name="Number of Ligand Atoms", accessor='ligand.nb_atoms')
    virus_name = tables.Column(verbose_name="Virus Name", accessor='protein.virus_name')
    protein_name = tables.Column(verbose_name = "Protein (pdb file)", accessor='protein.protein_name', linkify=('download', [tables.A('protein.pdb_file')]), empty_values=())
    protein_active_site = tables.Column(verbose_name="Protein Active Site Coordinates", accessor='protein.coor_file', linkify=('download', [tables.A('protein.coor_file')]), empty_values=())
    sdf_file_link = tables.Column(verbose_name="Pose SDF File", accessor="sdf_file", linkify=('download', [tables.A('sdf_file')]), empty_values=())
    binding_affinity=tables.Column(verbose_name="Binding Affinity")
    class Meta:
        model = Pose
        fields = ("binding_affinity",)
        sequence = ('virus_name', 'protein_name', 'protein_active_site', 'zinc_id', 'num_atoms', 'sdf_file_link', 'binding_affinity')

    # Un-comment this to put download link into csv download rather than just file name.
    # def value_sdf_file_link(self, record):
    #     return Site.objects.get_current().domain + reverse('download', kwargs={'filename': record.sdf_file})


class FilteredPoseView(SingleTableMixin, FilterView):
    table_class = PoseTable
    model = Pose
    template_name = "search/includes/filtered_table.html"

    filterset_class = PoseFilter
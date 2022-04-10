import django_tables2 as tables
from django.urls import reverse
from django.contrib.sites.models import Site
from .models import *

class PoseTable(tables.Table):
    """Table class for the Pose model"""
    zinc_id = tables.Column(verbose_name="Ligand ZINC ID", accessor='ligand.zinc_id') #ZINC ID, accessed through the ligand foreign key

    num_atoms = tables.Column(verbose_name="Number of Ligand Atoms", accessor='ligand.nb_atoms') #Number of atoms, accessed through the ligand foreign key

    virus_name = tables.Column(verbose_name="Virus Name", accessor='protein.virus_name') #Virus name, accessed through the protein foreign key

    protein_name = tables.Column(verbose_name = "Protein (pdb file)", accessor='protein.protein_name', #Protein name, accessed through the protein foreign key
        linkify=('download', [tables.A('protein.pdb_file')]), empty_values=()) #Render as a clickable link, which generates a url for the 'download' pattern using the protein's pdb_file field

    protein_active_site = tables.Column(verbose_name="Protein Active Site Coordinates", accessor='protein.coor_file', #Protein active site coordinates file name
        linkify=('download', [tables.A('protein.coor_file')]), empty_values=()) #Render as a clickable link, which generates a url for the 'download' pattern using the protein's coor_file field

    sdf_file_link = tables.Column(verbose_name="Pose SDF File", accessor="sdf_file", #Pose SDF file name
        linkify=('download', [tables.A('sdf_file')]), empty_values=()) #Render as a clickable link, which generates a url for the 'download' pattern using the sdf_file field

    binding_affinity=tables.Column(verbose_name="Binding Affinity") #Binding affinity

    class Meta:
        model = Pose
        fields = () #Do not use any default columns generated from the Pose fields
        sequence = ('virus_name', 'protein_name', 'protein_active_site', 'zinc_id', 'num_atoms', 'sdf_file_link', 'binding_affinity') #Sequence of display for columns defined above

    # Un-comment this to put download link into csv download rather than just file name.
    # def value_sdf_file_link(self, record):
    #     return Site.objects.get_current().domain + reverse('download', kwargs={'filename': record.sdf_file})
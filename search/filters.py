import django_filters
from .models import *

class PoseFilter(django_filters.FilterSet):
    """FilterSet class for the Pose model"""
    protein__virus_name = django_filters.AllValuesFilter(label="Virus Name") #Dropdown filter field by virus name, accessed through foreign key

    protein__protein_name = django_filters.AllValuesFilter(label="Protein Name") #Dropdown filter field by protein name, accessed through foreign key

    ligand__zinc_id = django_filters.CharFilter(label="Ligand ZINC ID") #Fill-in filter field by ligand ZINC ID, accessed through foreign key

    binding_affinity = django_filters.RangeFilter(label="Binding Affinity Range", #Range filter field by binding affinity
        widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'Binding affinity'})) #Widget to display placeholder text inside form

    class Meta:
        model = Pose
        fields = ['protein__virus_name', 'protein__protein_name', 'ligand__zinc_id', 'binding_affinity']
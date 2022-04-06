import django_filters
from .models import *

class PoseFilter(django_filters.FilterSet):
    protein__virus_name = django_filters.AllValuesFilter(label="Virus Name")
    protein__protein_name = django_filters.AllValuesFilter(label="Protein Name")
    ligand__zinc_id = django_filters.CharFilter(label="Ligand ZINC ID")
    binding_affinity = django_filters.RangeFilter(label="Binding Affinity Range", widget=django_filters.widgets.RangeWidget(attrs={'placeholder': 'Binding affinity'}))
    class Meta:
        model = Pose
        fields = ['protein__virus_name', 'protein__protein_name', 'ligand__zinc_id', 'binding_affinity']
import django_filters
from .models import *

class PoseFilter(django_filters.FilterSet):
    protein__virus_name = django_filters.AllValuesFilter()
    protein__protein_name = django_filters.AllValuesFilter()
    binding_affinity = django_filters.RangeFilter()
    class Meta:
        model = Pose
        fields = ['protein__virus_name', 'protein__protein_name', 'ligand__zinc_id', 'binding_affinity']
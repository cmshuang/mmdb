import django_filters
from .models import *

class PoseFilter(django_filters.FilterSet):
    class Meta:
        model = Pose
        fields = '__all__'
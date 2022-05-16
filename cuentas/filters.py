import django_filters
from django_filters import DateFilter

from .models import *


class OrdenFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Orden
        fields = '__all__'
        exclude = ['cliente', 'date_created']
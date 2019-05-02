import django_filters
from .models import *

class SchoolFilter(django_filters.FilterSet):
    ''' Filter for schools '''
    #name = django_filters.CharFilter(lookup_expr='iexact')
    # exact lookups for both the 'state' and 'lga' fields.
    class Meta:
        model = School
        fields = ['state', 'lga']    
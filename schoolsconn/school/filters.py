from django import forms
import django_filters
from .models import *

class SchoolFilter(django_filters.FilterSet):
    ''' Filter for schools '''
    # name = django_filters.CharFilter(lookup_expr='iexact')
    # exact lookups for both the 'state' and 'lga' fields.
    class Meta:
        model = School
        fields = ['state', 'lga', 'boarding', 'gender']     # 'creche', 'nursery', 'primary', 'secondary', 'aLevels']    

        # filter_overrides = {            
        #     models.BooleanField: {
        #         'filter_class': django_filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     },
        # }
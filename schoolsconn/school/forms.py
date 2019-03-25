from django import forms  
from .models import School, SchoolsConnBaseUser, BasicSchoolInfo, AdvancedSchoolInfo  


class SchoolForm(forms.ModelForm): 
    '''Form definition for the School Model.'''
    class Meta:  
        model = School  
        fields = ['email', 'name', 'phone', ]
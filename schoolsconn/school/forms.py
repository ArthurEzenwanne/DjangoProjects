from django import forms  
from .models import *

class SchoolForm(forms.ModelForm): 
    '''Form definition for the School Model.'''
    class Meta:  
        model = School  
        #fields = '__all__' #['email', 'name', 'phone', ]
        exclude = ['slug', 'user']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'lc-add-listing-input cpdl-map','placeholder':'Ex: admissions@adebanjohighschools.com'}),
            'name': forms.TextInput(attrs={'class':'lc-add-listing-input cpdl-map', 'placeholder':'Ex: Adebanjo Int\'l High School'}),
            'phone': forms.TextInput(attrs={'class':'lc-add-listing-input cpdl-map', 'placeholder':'Ex: 09090587701'}),
        }


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)        
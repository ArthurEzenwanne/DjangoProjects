from django import forms  
from .models import *

class SchoolForm(forms.ModelForm): 
    '''Form definition for the School Model.'''
    class Meta:  
        model = School  
        #fields = '__all__' #['email', 'name', 'phone', ]
        exclude = ['slug', 'user', 'city']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'lc-add-listing-input','placeholder':'Ex: admissions@adebanjohighschools.com'}),
            'name': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Adebanjo Int\'l High School'}),
            'phone': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: 09090587701'}),
            'motto': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Knowledge for Service'}),
            'description': forms.Textarea(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: A short description of your school, includining its mission and vission if available', 'height':'70px'}),
            'street': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: 11, Osibanjo Avenue, Alaka Estate'}),
            'town': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Ogba'}),
            #'city': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Ogba'}),
            'lga': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Ikeja'}),
            'state': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Lagos'}),
            'country': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Nigeria', 'value':'Nigeria'}),
            'approval_number': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: LA/IKD/2321'}),
            'admin': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Adamu Okoye'}),
            'website': forms.URLInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: http://www.adebanjohighschools.com'}),
            'founded': forms.DateInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: dd/mm/yyyy --> 22/04/2009'}),
            'boarding': forms.Select(attrs={'class':'lc-add-listing-input'}),
            'gender': forms.Select(attrs={'class':'lc-add-listing-input'}),
        }


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)        
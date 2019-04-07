from django import forms  
from .models import *

class SchoolForm(forms.ModelForm): 
    '''Form definition for the School Model.'''
    class Meta:  
        model = School  
        #fields = '__all__' #['email', 'name', 'phone', ]
        exclude = ['slug', 'user', 'city']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'lc-add-listing-input form-control','placeholder':'Ex: admissions@adebanjohighschools.com'}),
            'name': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Adebanjo Int\'l High School'}),
            'phone': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: 09090587701'}),
            'motto': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Knowledge for Service'}),
            'website': forms.URLInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: http://www.adebanjohighschools.com'}),
            
            'street': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: 11, Osibanjo Avenue, Alaka Estate'}),
            'town': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Ogba'}),
            #'city': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Ogba'}),
            'lga': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Ikeja'}),
            'state': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Lagos'}),
            'country': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Nigeria', 'value':'Nigeria'}),

            'approval_number': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: LA/IKD/2321'}),
            'admin': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Adamu Okoye'}),
            'founded': forms.DateInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: yyyy-mm-dd --> 2006-04-19'}),

            'boarding': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
            'gender': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
            'description': forms.Textarea(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: A short description of your school, includining its mission and vission if available', 'cols': 80, 'rows': 20}),
            
            'latitude': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'id':'lat', 'name':'latitude', 'placeholder':'Ex: -31.365486575872'}),
            'longitude': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'id':'lng', 'name':'longitude', 'placeholder':'Ex: 1.87676857332'}),
        }


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)        


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['uploaded_at']
        widgets = {
            'description': forms.TextInput(attrs={'class':'lc-add-listing-input form-control','placeholder':'Description of the image'}),
            'document': forms.FileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'desc_multiple': forms.TextInput(attrs={'class':'lc-add-listing-input form-control','placeholder':'Description of the image'}),
            'doc_multiple': forms.FileInput(attrs={'class':'lc-add-listing-input form-control', 'multiple': True})
        }
              
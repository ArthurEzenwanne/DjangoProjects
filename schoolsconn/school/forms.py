from django import forms  
from .models import *

class SchoolForm(forms.ModelForm): 
    '''Form definition for the School Model.'''
    class Meta:  
        model = School  
        #fields = '__all__' #['email', 'name', 'phone', ]
        exclude = ['slug', 'user', 'city', 'verified']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'lc-add-listing-input form-control','placeholder':'Ex: admissions@adebanjohighschools.com'}),
            'name': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Adebanjo Int\'l High School'}),
            'phone': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: 09090587701'}),
            'motto': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Knowledge for Service'}),
            'website': forms.URLInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: http://www.adebanjohighschools.com'}),
            
            'street': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: 11, Osibanjo Avenue, Alaka Estate'}),
            'town': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Ogba'}),
            #'city': forms.TextInput(attrs={'class':'lc-add-listing-input', 'placeholder':'Ex: Ogba'}),
            # 'lga': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Ikeja'}),
            # 'state': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Lagos'}),
            'lga': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
            'state': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
            'country': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Nigeria', 'value':'Nigeria'}),

            'approval_number': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: LA/IKD/2321'}),
            'admin': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: Adamu Okoye'}),
            'founded': forms.DateInput(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: yyyy-mm-dd --> 2006-04-19'}),

            'boarding': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
            'gender': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
            'description': forms.Textarea(attrs={'class':'lc-add-listing-input form-control', 'placeholder':'Ex: A short description of your school, includining its mission and vission if available', 'cols': 80, 'rows': 20}),
            
            'latitude': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'id':'lat', 'name':'latitude', 'placeholder':'Ex: -31.365486575872'}),
            'longitude': forms.TextInput(attrs={'class':'lc-add-listing-input form-control', 'id':'lng', 'name':'longitude', 'placeholder':'Ex: 1.87676857332'}),

            'logo': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
        }

class SearchForm(forms.Form): 
    '''Form definition for the Search Form.'''
    state = forms.ChoiceField()
    lga = forms.ChoiceField()

    # School Choice Region
    creche = forms.BooleanField(required=False)
    nursery = forms.BooleanField(required=False)
    primary = forms.BooleanField(required=False)
    secondary = forms.BooleanField(required=False)
    aLevels = forms.BooleanField(label='A-Levels', required=False)

    class Meta: 
        widgets = {
            'state': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
            'lga': forms.Select(attrs={'class':'lc-add-listing-input form-control'}),
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
            'document': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
        }

class DocumentMultipleForm(forms.ModelForm):
    class Meta:
        model = DocumentMultiple
        exclude = ['uploaded_at']
        widgets = {
            'desc_multiple': forms.TextInput(attrs={'class':'lc-add-listing-input form-control','placeholder':'Description of the image'}),
            'doc_multiple': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control', 'multiple': True})
        }

class SchoolGalleryForm(forms.ModelForm):
    '''Form definition for the SchoolGalleryImage Model.'''

    class Meta:
        model = SchoolGalleryImage
        exclude = ['uploaded_at']
        widgets = {
            'img_1': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_2': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_3': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_4': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_5': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_6': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_7': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_8': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_9': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_9': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'img_10': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
            'banner_img': forms.ClearableFileInput(attrs={'class':'lc-add-listing-input form-control'}),
        }        
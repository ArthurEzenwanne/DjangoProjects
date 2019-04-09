import re
from PIL import Image
from io import StringIO, BytesIO
from django.core.files.base import ContentFile
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect  
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.core.files import File

from .models import *
from .forms import *

# Create your views here.
# from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""


    return render(request, 'index.html')


# def school_detail_view(request, slug):
#     """Function based detailed view for School model."""
#     school = get_object_or_404(School, slug=slug)
#     return render(request, 'school/school_detail.html', context={'school': school})      

class SchoolDetailView(generic.DetailView):
    """Class based detailed view for School model."""
    model = School    

class SchoolListView(generic.ListView):
    """Class based list view for School model."""
    model = School
    paginate_by = 30    

# def account_profile_view(request, email):
#     """Function based view for user profile model."""
#     user = get_object_or_404(SchoolsConnBaseUser, email=self.email)
#     return render(request, 'school/admin/user-profile.html', context={'user': user})     

# def account_schools_view(request):
#     """Function based view for user's listed schools."""
#     #user = get_object_or_404(SchoolsConnBaseUser, username=username)    
#     #school = get_list_or_404(School, request.user)
#     school_set = School.objects.filter(user=request.user)
#     return render(request, 'school/admin/school-listing.html', context={'school': school_set})     

#@method_decorator(login_required)
class AccountsSchoolsListView(LoginRequiredMixin, generic.ListView):
    """Class View to display Schools created by user."""
    model = School
    template_name = 'school/admin/school-listing.html'
    context_object_name = 'all_schools_by_user'

    def get_queryset(self):
        return School.objects.filter(user=self.request.user)

def slugify(s):
    """
    Simplifies ugly strings into something URL-friendly.
    """
    s = s.lower()
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')
    s = re.sub('\W', '', s)
    s = s.replace('_', ' ')
    s = re.sub('\s+', ' ', s)
    s = s.strip()
    s = s.replace(' ', '-')
    return s

@login_required  
def create_school(request):
    """View function for creating a School instance outside the user admin."""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SchoolForm(request.POST, request.FILES)  
   
        # check whether it's valid:
        if form.is_valid():  
            # process the data in form.cleaned_data as required
            school = form.save(commit=False) 
            school.user = request.user  
            school.slug = slugify(school.name)

            ##!!! DO NOT EDIT THE FILE, OR RESIZE THE FILE HERE, IT IS TOO MUCH WORK. TRY RESIZE THE FILES
            ##!!! ON THE CLIENT USING JSCRIPT OR JQUERY, ANY IMAGE SENT HERE SHOULD BE THE FINALE IMAGE !!!###

            # if school.logo:
            #     logo = request.FILES['logo']
            #     fs = FileSystemStorage()            # Works when media is handled on local fileSystem
            #     filename = fs.save(logo.name, logo)
            #     uploaded_file_url = fs.url(filename)
            school.save()


        # redirect to a new URL:
        return redirect('school-listing')    
    # if a GET (or any other method) we'll create a blank form  
    else:
        form = SchoolForm()    
        return render(request, 'school/create_school.html', {'form': form})



@login_required  
def add_school(request):
    """View function for creating a School instance on the user admin."""
    #create v1 csharpconer
    form = SchoolForm(request.POST or None)  
   
    if form.is_valid():          
        school = form.save(commit=False)  
        school.user = request.user  
        school.slug = slugify(school.name)
        school.logo = form.cleaned_data['logo']
        #logo = School(logo=request.FILES['logo'])        
        #school.logo = School(logo=request.FILES['logo'])
        #logo.save()
        school.save()
        
        # Increament number of schools created by the user
        # num_schools = SchoolsConnBaseUser.schools.value_from_object()
        # num_schools = num_schools + 1
        # SchoolsConnBaseUser.schools = num_schools
        # SchoolsConnBaseUser.save()
        return redirect('school-listing')  
    return render(request, 'school/add_school.html', {'form': form})    

    #create v2 javapoint
    # if request.method == "POST":  
    #     form = EmployeeForm(request.POST)  
    #     if form.is_valid():  
    #         try:  
    #             form.save()  
    #             return redirect('/show')  
    #         except:  
    #             pass  
    # else:  
    #     form = EmployeeForm()  
    # return render(request,'index.html',{'form':form})  

@login_required  
def update_school(request, slug):  
    """View function for updating a School instance."""
    if request.user.is_superuser:  
        school = get_object_or_404(School, slug=slug)  
    else:  
        school = get_object_or_404(School, slug=slug, user=request.user)  
    form = SchoolForm(request.POST or None, instance=school)  
    if form.is_valid():  
        school = form.save(commit=False) 
        school.slug = slugify(school.name)
        school.save()
        return redirect('school-listing')  
    return render(request, 'school/edit_school.html', {'form': form}) 
  
@login_required  
def delete_school(request, slug):  
    """View function for deleting a School instance."""
    if request.user.is_superuser:  
        school = get_object_or_404(School, slug=slug)  
    else:  
        school = get_object_or_404(School, slug=slug, user=request.user)  
    if request.method == 'POST':  
        school.delete()  
        return redirect('school-listing')  
    return render(request, 'school/admin/delete_school.html', {'object': school})        


def thanks(request):  
    """View function for deleting a School instance."""
    
    return render(request, 'school/thanks.html') 

from django.core.mail import send_mail

def send_mail_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'school/send_mail_form_two.html', {'form': form})

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'school/simple_upload.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'school/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # description=request.POST.get('description')) or description=form.cleaned_data['description'] works
            instance = Document(document=request.FILES['document'], description=form.cleaned_data['description'])
            instance.save()
            return render(request, 'school/model_form_upload.html', {'instance': instance})   
            #return HttpResponseRedirect('index')
    else:
        form = DocumentForm()
    return render(request, 'school/model_form_upload.html', {'form': form})    

def model_form_upload_multiple(request):
    # This works for multiple files
    document = DocumentMultiple.objects.all()
    if request.method == 'GET':
        form = DocumentMultipleForm(None)
    elif request.method == 'POST':
        for _file in request.FILES.getlist('doc_multiple'):
            request.FILES['doc_multiple'] = _file
            form = DocumentMultipleForm(request.POST, request.FILES)
            if form.is_valid():
                _new = form.save(commit=False)
                _new.save()
                form.save_m2m()
    return render(request, 'school/multiple_model_form_upload.html', {'form': form, 'document': document})          

def model_upload_multiple(request):
    # This works for multiple files
    if request.method == 'POST':
        form = DocumentMultipleForm(request.POST, request.FILES)
        if form.is_valid():
            desc_multiple = form.cleaned_data['desc_multiple']

            # This If statement works
            for f in request.FILES.getlist('doc_multiple'):
                DocumentMultiple.objects.create(desc_multiple=desc_multiple, doc_multiple=f)
             
            # This If statement doesn't works
            # for f in request.FILES.getlist('desc_multiple'):
            #     instance = DocumentMultiple.objects.create(desc_multiple=desc_multiple, doc_multiple=f)
            #     instance.save()
                
            return render(request, 'school/model_form_upload.html', {'form': form})                
    else:
        form = DocumentMultipleForm()
    return render(request, 'school/multiple_model_form_upload.html', {'form': form})    
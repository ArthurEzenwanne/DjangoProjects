import re
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect  
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.utils.decorators import method_decorator
from .models import School, SchoolsConnBaseUser, BasicSchoolInfo, AdvancedSchoolInfo
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
    """View function for creating a School instance."""
    #create v1 csharpconer
    form = SchoolForm(request.POST or None)  
   
    if form.is_valid():  
        school = form.save(commit=False)  
        school.user = request.user  
        school.slug = slugify(school.name)
        school.save()
        return redirect('school-listing')  
    return render(request, 'school/create_school_form.html', {'form': form})

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
def edit_school(request, id):
    """View function for editing a School instance."""
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

@login_required  
def update_school(request, id):  
    """View function for updating a School instance."""
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

@login_required  
def delete_school(request, id):  
    """View function for deleting a School instance."""
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")          
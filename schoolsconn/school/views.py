from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import School, SchoolsConnBaseUser, BasicSchoolInfo, AdvancedSchoolInfo

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

def account_profile_view(request, email):
    """Function based view for user profile model."""
    user = get_object_or_404(SchoolsConnBaseUser, email=self.email)
    return render(request, 'school/admin/profile-blue.html', context={'user': user})     
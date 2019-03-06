from django.shortcuts import render, get_object_or_404, get_list_or_404
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

class AccountsSchoolsListView(generic.ListView):
    model = School
    template_name = 'school/admin/school-listing.html'
    context_object_name = 'all_schools_by_user'

    def get_queryset(self):
        return School.objects.filter(user=self.request.user)    
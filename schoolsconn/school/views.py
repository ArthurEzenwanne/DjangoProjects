from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import School

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
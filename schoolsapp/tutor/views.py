from django.shortcuts import render, get_object_or_404
from django.views import generic

from tutor.models import Tutor, Experience, Education, School

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # The 'all()' is implied by default, so we can leave it out
    num_tutors = Tutor.objects.all().count()
        
    context = {        
        'num_tutors': num_tutors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def search(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # The 'all()' is implied by default, so we can leave it out
    num_tutors = Tutor.objects.all().count()
        
    context = {        
        'num_tutors': num_tutors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class TutorListView(generic.ListView):
    """Class based list view for Tutor model."""
    model = Tutor

class TutorDetailView(generic.DetailView):
    """Class based detailed view for Tutor model."""
    model = Tutor        

def tutor_detail_view(request, username):
    tutor = get_object_or_404(Tutor, username=username)
    return render(request, 'tutor/tutor_detail.html', context={'tutor': tutor})    

def school_detail_view(request, slug):
    school = get_object_or_404(School, slug=slug)
    return render(request, 'school/school_detail.html', context={'school': school})       

class SchoolListView(generic.ListView):
    """Class based list view for School model."""
    model = School

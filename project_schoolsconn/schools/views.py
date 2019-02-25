from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # The 'all()' is implied by default, so we can leave it out
    # num_tutors = Tutor.objects.all().count()
        
    # context = {        
    #     'num_tutors': num_tutors,
    # }

    # Render the HTML template index.html with the data in the context variable
    # return render(request, 'index.html', context=context)
    return render(request, 'index.html')
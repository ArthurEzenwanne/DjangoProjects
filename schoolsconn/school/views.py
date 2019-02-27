from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models

# Create your views here.
# from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""


    return render(request, 'index.html')



def school_detail_view(request, slug):
    school = get_object_or_404(School, slug=slug)
    return render(request, 'school/school_detail.html', context={'school': school})      
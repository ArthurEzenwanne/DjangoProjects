from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tutors/', views.TutorListView.as_view(), name='tutors'),
    # path('tutor/<str:username>', views.TutorDetailView.as_view(), name='tutor-detail'),
    path('tutor/<str:username>', views.tutor_detail_view, name='tutor-detail'),
    # The generic class-based detail view expects to be passed a parameter named pk. 
    # If you're writing your own function view you can use whatever parameter name you like, 
    # or indeed pass the information in an unnamed argument.

    
    path('schools/', views.SchoolListView.as_view(), name='schools'),    
    path('school/<str:slug>', views.school_detail_view, name='school-detail'),
]

# Generic detail view TutorDetailView must be called with either an object pk or a slug in the URLconf.
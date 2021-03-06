"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

from . import views

#from .models import School, SchoolsConnBaseUser

#admin.autodiscover()

urlpatterns = [
    path('', views.index, name='index'),
    path('test/search/', views.search_filter_view, name='search-filter'), # works
    path('search/schools/', views.SchoolListView.as_view(), name='schools-list'), # works but no filter
    path('search/schools/<state>/', views.FilterSchoolsByStatesListView.as_view(), name='filter-schools-state-list'),
    path('schools/<str:slug>/', views.SchoolDetailView.as_view(), name='school-detail'), # uses slug, could also use pk
    #path('accounts/profile', views.account_profile_view, name='account-profile'),   # routes to the profile view
    #path('accounts/profile', TemplateView.as_view(template_name='school/admin/user-profile.html'), name='user-profile'),
    #path('accounts/profile/', login_required(TemplateView.as_view(template_name='school/admin/user-profile.html')), name='user-profile'),
    #path('accounts/schools/', TemplateView.as_view(template_name='school/admin/school-listing.html'), name='school-listing'),
    #path('accounts/profile/', TemplateView.as_view(template_name='school/admin/user-profile.html'), name='user-profile'),
    path('accounts/profile/', views.ProfileView.as_view(), name='user-profile'),
    #path('accounts/schools/', views.account_schools_view, name='school-listing'),
    path('accounts/schools/', views.AccountsSchoolsListView.as_view(), name='school-listing'),
    path('accounts/schools/add/', views.add_school, name='add-school'),

    path('school/new/', views.create_school_view, name='create-school'),
    path('school/edit/<str:slug>/', views.update_school, name='update-school'),
    path('school/delete/<str:slug>/', views.delete_school, name='delete-school'),
    # path('school/gallery/add/', views.add_gallery, name='add-gallery'),     # add gallery images

    path('contactus/', views.send_mail_view, name='contact-us'), 
    path('thanks/', views.thanks, name='thanks'), 
    path('upload/', views.simple_upload, name='file-upload'),
    path('model-upload/', views.model_form_upload, name='model-upload'),
    path('model-upload-multiple/', views.model_upload_multiple, name='model-upload-multiple'),
]

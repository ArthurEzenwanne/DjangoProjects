from django.contrib import admin
from .models import SchoolsConnBaseUser

# Register your models here.

class SchoolsConnUserAdmin(admin.ModelAdmin):
    '''
    Model admin for a custom user
    '''
    pass

admin.site.register(SchoolsConnBaseUser, SchoolsConnUserAdmin)
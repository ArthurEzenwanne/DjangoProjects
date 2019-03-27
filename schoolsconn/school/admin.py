from django.contrib import admin
from .models import *

# Register your models here.

class SchoolsConnUserAdmin(admin.ModelAdmin):
    '''
    Model admin for a custom user
    '''
    pass

admin.site.register(SchoolsConnBaseUser, SchoolsConnUserAdmin)

# class BasicSchoolInfoInline(admin.StackedInline):
#     model = BasicSchoolInfo
#     extra = 0
#     # These could also accept same attributes such as fields and fieldsets etc

# class AdvancedSchoolInfoInline(admin.StackedInline):
#     model = AdvancedSchoolInfo
#     extra = 0 

# Register the Admin classes for School using the decorator
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'phone', 'email')
    list_filter = ('name', 'email')

    # fields = [('first_name', 'last_name'), ('email_address', 'username'), ('phone_num', 'years_of_experience')]

    """ fieldsets = (
        ('Personal Details', {
            'fields': [('first_name', 'last_name')]
        }),
        ('Others', {
            'fields': [('email_address', 'username'), ('phone_num', 'years_of_experience')]
        }),
    ) """

    #inlines = [BasicSchoolInfoInline, AdvancedSchoolInfoInline]

# Register the Admin classes for BasicSchoolInfo using the decorator
# @admin.register(BasicSchoolInfo)
# class BasicSchoolInfoAdmin(admin.ModelAdmin):
#     list_display = ('school', 'approval_number', 'founded')
    
# # Register the Admin classes for AdvancedSchoolInfo using the decorator
# @admin.register(AdvancedSchoolInfo)
# class AdvancedSchoolInfoAdmin(admin.ModelAdmin):
#     list_display = ('school', 'activities', 'clubs')        
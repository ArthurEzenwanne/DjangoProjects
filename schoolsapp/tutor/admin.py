from django.contrib import admin

from tutor.models import Tutor, Education, Experience, School

# Register your models here.

# admin.site.register(Tutor)
# admin.site.register(Education)
# admin.site.register(Experience)
admin.site.register(School)

class EducationInline(admin.StackedInline):
    model = Education
    extra = 0
    # These could also accept same attributes such as fields and fieldsets etc

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 0 

# Register the Admin classes for Tutor using the decorator
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email_address', 'phone_num', 'years_of_experience')
    list_filter = ('email_address', 'username', 'years_of_experience')

    # fields = [('first_name', 'last_name'), ('email_address', 'username'), ('phone_num', 'years_of_experience')]

    fieldsets = (
        ('Personal Details', {
            'fields': [('first_name', 'last_name')]
        }),
        ('Others', {
            'fields': [('email_address', 'username'), ('phone_num', 'years_of_experience')]
        }),
    )

    inlines = [ExperienceInline, EducationInline]

# Register the Admin classes for Experience using the decorator
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'organization', 'job_position')
    
# Register the Admin classes for Education using the decorator
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('tutor', 'institution', 'qualification')        
from django.contrib import admin

from tutor.models import Tutor, Education, Experience

# Register your models here.

admin.site.register(Tutor)
admin.site.register(Education)
admin.site.register(Experience)
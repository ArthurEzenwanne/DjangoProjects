import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

# https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/fields/#django.contrib.postgres.fields.ArrayField
# Note ArrayFields when using PostGress

# Create your models here.
class SchoolsConnBaseUser(AbstractUser):
    '''Model for a custom user.'''
    phone = models.CharField(max_length=20, null=True, blank=True)  
    fname = models.CharField(max_length=20, null=True, blank=True) 
    lname = models.CharField(max_length=20, null=True, blank=True) 
    street = models.CharField(max_length=20, null=True, blank=True) 
    town = models.CharField(max_length=20, null=True, blank=True) 
    lga = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True) 
    country = models.CharField(max_length=20, default='Nigeria') 
    schools = models.SmallIntegerField(default=0, editable=False, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.fname} {self.lname}'

class School(models.Model):
    """Model representing a school."""
    email = models.EmailField(max_length=128)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    slug = models.SlugField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(SchoolsConnBaseUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular school instance."""
        # return reverse('tutor-detail', args=[str(self.email_address)])
        return reverse('school-detail', args=[str(self.id)]) # school-detail is a view

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

class BasicSchoolInfo(models.Model):
    """Model representing a schools's basic information."""
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    motto = models.CharField(max_length=256, blank=True, null=True, default='N/A')
    description = models.CharField(max_length=1000, blank=True, null=True, default='No description yet...')

    country = models.CharField(max_length=50, default='Nigeria')
    state = models.CharField(max_length=50) #, blank=True, null=True, default='Lagos')
    lga = models.CharField(max_length=50) #, blank=True, null=True, default='N/A')
    city = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=640)

    SCHOOL_TYPE_CHOICE = (
        ('c', 'Creche'),
        ('np', 'Nursery-Primary'),
        ('s', 'Secondary'),
        ('al', 'A-Levels'),
    )

    APPROVED_EXAM_CHOICE = (
        ('ncce', 'National Common Entrance Examinations'),
        ('scce', 'State Common Entrance Examinatins'),
        ('waec', 'West African Examination Council Exams'),
        ('neco', 'National Examinations Council Exams'),        
        ('jwaec', 'Junior West African Examination Council Exams'),
        ('jneco', 'Junior National Examinations Council Exams'),
        ('toefl', 'TOEFL Exams'),
        ('ielts', 'IELTS Exams'),
        ('alevel', 'A-Levels Exams'),
        ('igcse', 'IGCSE Exams'),
    )

    GENDER_CHOICE = (
        ('m', 'Male Only'),
        ('f', 'Female Only'),
        ('mx', 'Mixed'),
    )

    BOARDING_CHOICE = (
        ('fb', 'Full Boarding'),
        ('fd', 'Day Only'),
        ('bd', 'Day and Boarding'),
    )

    approval_number = models.CharField(max_length=11, default='Awaiting')
    admin = models.CharField(max_length=128, default='N/A')
    school_type = models.CharField(max_length=2, choices=SCHOOL_TYPE_CHOICE, default='np')
    approved_exams = models.CharField(max_length=6, choices=APPROVED_EXAM_CHOICE, default='ncce')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default='mixed')
    boarding = models.CharField(max_length=2, choices=BOARDING_CHOICE, default='bd')
    founded = models.DateField(default='N/A')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.school}'

class AdvancedSchoolInfo(models.Model):
    """Model representing a schools's advanced information."""
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    ACTIVITY_CHOICE = (
        ('c', 'Creche'),
        ('np', 'Nursery-Primary'),
        ('s', 'Secondary'),
        ('al', 'A-Levels'),
    )

    CLUB_CHOICE = (
        ('bscout', 'National Common Entrance Examinations'),
        ('gguide', 'State Common Entrance Examinatins'),
        ('frsc', 'West African Examination Council Exams'),
        ('music', 'National Examinations Council Exams'),        
        ('drama', 'Junior West African Examination Council Exams'),
        ('debate', 'Junior National Examinations Council Exams'),
        ('press', 'TOEFL Exams'),
        ('jets', 'IELTS Exams'),
        ('rcross', 'A-Levels Exams'),
        ('artscraft', 'IGCSE Exams'),
    )

    FACILITY_CHOICE = (
        ('sickbay', 'Sickbay'),
        ('multipurposehall', 'Multipurpose Hall'),
        ('sciencelab', 'Science Lab'),
        ('busservice', 'Bus Service'),
        ('library', 'Library'),
        ('playground', 'Playground'),
        ('sportscomplex', 'Sports Complex'),
        ('ictcenter', 'ICT Center'),
        ('artstudio', 'Art Studio'),
        ('elibrary', 'E-Library'),
        ('swimmingpool', 'Swimming Pool'),
        ('orchard', 'Orchard'),
        ('farmhouse', 'Farmhouse'),
        ('specialneeds', 'Special Needs Care'),
        ('musicstudio', 'Music Studio'),
        ('stem', 'STEM'),
        ('homemanagementlab', 'Home Management Lab'),
        ('languagestudio', 'Language Studio'),
    )

    school_type = models.CharField(max_length=2, choices=SCHOOL_TYPE_CHOICE, default='np')
    approved_exams = models.CharField(max_length=6, choices=APPROVED_EXAM_CHOICE, default='ncce')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE, default='mixed')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.school}'

    

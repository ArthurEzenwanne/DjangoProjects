import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.urls import reverse

# Create your models here.
class SchoolsConnBaseUser(AbstractUser):
    '''
    Model for a custom user
    '''
    phone = models.CharField(max_length=20)  

# class Tutor(models.Model):
#     """Model representing a tutor."""
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email_address = models.EmailField(max_length=100, primary_key=True)
#     phone_num = models.CharField(max_length=15)
#     years_of_experience = models.IntegerField(default=0)
#     username = models.CharField(max_length=50, unique=True)

#     # class Meta:
#     #     ordering = ['last_name', 'first_name']
    
#     def get_absolute_url(self):
#         """Returns the url to access a particular tutor instance."""
#         # return reverse('tutor-detail', args=[str(self.email_address)])
#         return reverse('tutor-detail', args=[str(self.username)])

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.first_name} {self.last_name}'

# class Experience(models.Model):
#     """Model representing a tutor's experience."""
#     tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
#     organization = models.CharField(max_length=100, null=True, blank=True)
#     job_position = models.CharField(max_length=100, null=True, blank=True) 
#     location = models.CharField(max_length=100, null=True, blank=True)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     reponsibility = models.CharField(max_length=1000, null=True, blank=True)
#     awards = models.CharField(max_length=1000, null=True, blank=True)
#     specialization = models.CharField(max_length=100, null=True, blank=True)

#     # tutor.experience_set.create(
#     #     organization='org1',
#     #     position='position1',
#     # )
#     # tutor.experience_set.create(
#     #     organization='org2',
#     #     position='position2',
#     # )
#     # tutor.experience_set.create(
#     #     organization='org3',
#     #     position='position3',
#     # ) 
#     # This is to be used in dynamically creating the experiences for each signed in tutor #
#     # So we could have a new tutor 'Ada' ceating new  experiences as #
#     # Ada.experience_set.create (
#     #   organization='any organizational input user inputs',
#     #   position='any position input user inputs',
#     #   )#        

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.first_name} {self.last_name}'

# class Education(models.Model):
#     """Model representing a tutor's education."""
#     tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
#     #email_address = models.EmailField(null=False, blank=False, max_length=100, primary_key=True)
#     institution = models.CharField(max_length=100, null=True, blank=True)
#     course = models.CharField(max_length=100, null=True, blank=True)
#     qualification = models.CharField(max_length=50, null=True, blank=True)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     awards = models.CharField(max_length=1000, null=True, blank=True)

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.first_name} {self.last_name}'          

class School(models.Model):
    """Model representing a school."""
    email = models.EmailField(max_length=128)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    slug = models.SlugField(max_length=128)

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

    school_type_choice = (
        ('c', 'Creche'),
        ('np', 'Nursery-Primary'),
        ('s', 'Secondary'),
        ('al', 'A-Levels'),
    )

    approved_exam_choice = (
        ('ncce', 'National Common Entrance Examinations'),
        ('scce', 'State Common Entrance Examinatins'),
        ('waec', 'West African Examination Council Exams'),
        ('neco', 'National Examinations Council Exams'),
        ('tofel', 'TOFEL Exams'),
        ('ilets', 'ILETS Exams'),
    )

    gender_choice = (
        ('male', 'Male Only'),
        ('female', 'Female Only'),
        ('mixed', 'Mixed'),
    )

    boarding_choice = (
        ('fb', 'Full Boarding'),
        ('fd', 'Day Only'),
        ('bd', 'Day and Boarding'),
    )

    approval_number = models.CharField(max_length=11, default='Awaiting')
    admin = models.CharField(max_length=128, default='N/A')
    school_type = models.CharField(max_length=2, choices=school_type_choice, default='np')
    approved_exams = models.CharField(max_length=6, choices=approved_exam_choice, default='ncce')
    gender = models.CharField(max_length=6, choices=gender_choice, default='mixed')
    boarding = models.CharField(max_length=2, choices=boarding_choice, default='bd')
    founded = models.DateField(default='N/A')

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
import datetime
from datetime import date
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

class Tutor(models.Model):
    """Model representing a tutor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, primary_key=True)
    phone_num = models.CharField(max_length=15)
    years_of_experience = models.IntegerField(default=0)
    username = models.CharField(max_length=50, unique=True)

    # class Meta:
    #     ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular tutor instance."""
        # return reverse('tutor-detail', args=[str(self.email_address)])
        return reverse('tutor-detail', args=[str(self.username)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class Experience(models.Model):
    """Model representing a tutor's experience."""
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, null=True, blank=True)
    job_position = models.CharField(max_length=100, null=True, blank=True) 
    location = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    reponsibility = models.CharField(max_length=1000, null=True, blank=True)
    awards = models.CharField(max_length=1000, null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)

    # tutor.experience_set.create(
    #     organization='org1',
    #     position='position1',
    # )
    # tutor.experience_set.create(
    #     organization='org2',
    #     position='position2',
    # )
    # tutor.experience_set.create(
    #     organization='org3',
    #     position='position3',
    # ) 
    # This is to be used in dynamically creating the experiences for each signed in tutor #
    # So we could have a new tutor 'Ada' ceating new  experiences as #
    # Ada.experience_set.create (
    #   organization='any organizational input user inputs',
    #   position='any position input user inputs',
    #   )#        

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class Education(models.Model):
    """Model representing a tutor's education."""
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    #email_address = models.EmailField(null=False, blank=False, max_length=100, primary_key=True)
    institution = models.CharField(max_length=100, null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=50, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    awards = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'          

class School(models.Model):
    """Model representing a school."""
    email_address = models.EmailField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    motto = models.CharField(max_length=1000, blank=True)
    description = models.CharField(max_length=1000)

    country = models.CharField(max_length=100, default='Nigeria')
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100)

    #telephone = models.CharField(max_length=17, unique=True, blank=True)
    telephone = models.CharField(max_length=17, blank=True, default='+2349090587701')
    approval_number = models.CharField(max_length=11, default='Awaiting')
    contact_person = models.CharField(max_length=100, default='Not Available')
    school_type = models.CharField(max_length=50, default='Nursery')
    approved_exams = models.CharField(max_length=50, default='NCEE')
    founded_date = models.DateField(null=True, blank=True, default=date.today)

    slug = models.SlugField(max_length=128, unique=True)

    def get_absolute_url(self):
        """Returns the url to access a particular school instance."""
        # return reverse('tutor-detail', args=[str(self.email_address)])
        return reverse('school-detail', args=[str(self.slug)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'
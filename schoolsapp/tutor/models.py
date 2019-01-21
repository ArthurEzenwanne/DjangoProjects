from django.db import models
from django.urls import reverse
# Create your models here.

class Tutor(models.Model):
    """Model representing a tutor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100, primary_key=True)
    phone_num = models.IntegerField()
    years_of_experience = models.IntegerField(default=0)
    username = models.CharField(max_length=50, unique=True)

    # class Meta:
    #     ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular tutor instance."""
        return reverse('tutor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

class Experience(models.Model):
    """Model representing a tutor's experience."""
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    #email_address = models.EmailField(null=False, blank=False, max_length=100, primary_key=True)
    organization_one = models.CharField(max_length=100, null=True, blank=True)
    job_position_one = models.CharField(max_length=100, null=True, blank=True)
    location_one = models.CharField(max_length=100, null=True, blank=True)
    start_date_one = models.DateField(null=True, blank=True)
    end_date_one = models.DateField(null=True, blank=True)
    reponsibility_one = models.CharField(max_length=1000, null=True, blank=True)
    awards_one = models.CharField(max_length=1000, null=True, blank=True)
    specialization_one = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'        

class Education(models.Model):
    """Model representing a tutor's education."""
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    #email_address = models.EmailField(null=False, blank=False, max_length=100, primary_key=True)
    institution_one = models.CharField(max_length=100, null=True, blank=True)
    course_one = models.CharField(max_length=100, null=True, blank=True)
    qualification_one = models.CharField(max_length=50, null=True, blank=True)
    start_date_one = models.DateField(null=True, blank=True)
    end_date_one = models.DateField(null=True, blank=True)
    awards_one = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'          
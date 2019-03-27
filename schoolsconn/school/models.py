import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.urls import reverse
#from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _

# https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/fields/#django.contrib.postgres.fields.ArrayField
# Note ArrayFields when using PostGress

# Create your models here.
class SchoolsConnBaseUser(AbstractUser):
    '''Model for a custom user.'''
    phone = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=20, null=True, blank=True) 
    town = models.CharField(max_length=20, null=True, blank=True) 
    lga = models.CharField(max_length=20, null=True, blank=True)
    state = models.CharField(max_length=20, null=True, blank=True) 
    country = models.CharField(max_length=20, default='Nigeria') 
    schools = models.SmallIntegerField(default=0, editable=False, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        #return f'{self.first_name} {self.last_name} {self.username} {self.email}'  # this works
        return f'{self.username}'
        
        
# class School(models.Model):
#     """Model representing a school."""
#     email = models.EmailField(max_length=128)
#     name = models.CharField(max_length=128)
#     phone = models.CharField(max_length=15)
#     slug = models.SlugField(max_length=128)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     user = models.ForeignKey(SchoolsConnBaseUser, on_delete=models.CASCADE)

#     # Basic Info 
#     motto = models.CharField(max_length=256, blank=True, null=True, default='N/A')
#     description = models.CharField(max_length=1000, blank=True, null=True, default='No description yet...')

#     country = models.CharField(max_length=50, default='Nigeria')
#     state = models.CharField(max_length=50, default='Lagos') #, blank=True, null=True, default='Lagos')
#     lga = models.CharField(max_length=50, default='Ikeja') #, blank=True, null=True, default='N/A')
#     city = models.CharField(max_length=50, null=True, blank=True)
#     town = models.CharField(max_length=50, null=True, blank=True)
#     street = models.CharField(max_length=640, default='11, Saka Tinubu Street')

#     SCHOOL_TYPE_CHOICE = (
#         ('c', 'Creche'),
#         ('n', 'Nursery'),
#         ('p', 'Primary'),
#         ('s', 'Secondary'),
#         ('al', 'A-Levels')
#     )

#     APPROVED_EXAM_CHOICE = (
#         ('ncce', 'National Common Entrance Examinations'),
#         ('scce', 'State Common Entrance Examinatins'),
#         ('waec', 'West African Examination Council Exams'),
#         ('neco', 'National Examinations Council Exams'),        
#         ('jwaec', 'Junior West African Examination Council Exams'),
#         ('jneco', 'Junior National Examinations Council Exams'),
#         ('toefl', 'TOEFL Exams'),
#         ('ielts', 'IELTS Exams'),
#         ('alevel', 'A-Levels Exams'),
#         ('igcse', 'IGCSE Exams')
#     )

#     GENDER_CHOICE = (
#         ('m', 'Male Only'),
#         ('f', 'Female Only'),
#         ('mx', 'Mixed')
#     )

#     BOARDING_CHOICE = (
#         ('fb', 'Full Boarding'),
#         ('fd', 'Day Only'),
#         ('bd', 'Day and Boarding')
#     )

#     approval_number = models.CharField(max_length=11, default='Awaiting')
#     admin = models.CharField(max_length=128, default='N/A')
#     school_type = MultiSelectField(choices=SCHOOL_TYPE_CHOICE, default='n') # max_choices not needed - use multi
#     approved_exams = MultiSelectField(choices=APPROVED_EXAM_CHOICE, default='ncce') # max_choices not needed - use multi
#     gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default='mx') # max_choices is 1 - use default
#     boarding = models.CharField(max_length=2, choices=BOARDING_CHOICE, default='bd') # max_choices is 1 - use default
#     #founded = models.DateField(auto_now_add=True)

#     # Advanced Info 
#     ACTIVITY_CHOICE = (
#         ('carol', 'Creche'),
#         ('interhousesports', 'Interhouse Sports'),
#         ('culturalday', 'Cultural Day'),
#         ('dance', 'Dance'),
#         ('spellingbees', 'Spelling Bees'),
#         ('debate', 'Debate'),
#         ('quiz', 'Quiz'),        
#         ('swimming', 'Swimming'),
#         ('karate', 'Karate'),
#         ('costumeday', 'Costume Day')
#     )

#     CLUB_CHOICE = (
#         ('bscout', 'Boys Scout'),
#         ('gguide', 'Girls Guide'),
#         ('frsc', 'FRSC Club'),
#         ('music', 'Music Club'),        
#         ('drama', 'Drama Club'),
#         ('debate', 'Debate Club'),
#         ('press', 'Press Club'),
#         ('jets', 'JETS Club'),
#         ('rcross', 'Red Cross'),
#         ('artscraft', 'Arts-Craft Club')
#     )

#     FACILITY_CHOICE = (
#         ('sickbay', 'Sickbay'),
#         ('multipurposehall', 'Multipurpose Hall'),
#         ('sciencelab', 'Science Lab'),
#         ('busservice', 'Bus Service'),
#         ('library', 'Library'),
#         ('playground', 'Playground'),
#         ('sportscomplex', 'Sports Complex'),
#         ('ictcenter', 'ICT Center'),
#         ('artstudio', 'Art Studio'),
#         ('elibrary', 'E-Library'),
#         ('swimmingpool', 'Swimming Pool'),
#         ('orchard', 'Orchard'),
#         ('farmhouse', 'Farmhouse'),
#         ('specialneeds', 'Special Needs Care'),
#         ('musicstudio', 'Music Studio'),
#         ('stem', 'STEM'),
#         ('homemanagementlab', 'Home Management Lab'),
#         ('languagestudio', 'Language Studio')
#     )

#     activities = MultiSelectField(choices=ACTIVITY_CHOICE, default='debate')
#     clubs = MultiSelectField(choices=CLUB_CHOICE, default='debate')
#     facilities = MultiSelectField(choices=FACILITY_CHOICE, default='playground')

#     def get_absolute_url(self):
#         """Returns the url to access a particular school instance."""
#         # return reverse('tutor-detail', args=[str(self.email_address)])
#         #return reverse('school-detail', args=[str(self.id)]) # school-detail is a view
#         return reverse('school-detail', args=[str(self.slug)]) # school-detail is a view

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.name}'

# class BasicSchoolInfo(models.Model):
#     """Model representing a schools's basic information."""
#     school = models.ForeignKey(School, on_delete=models.CASCADE)

#     motto = models.CharField(max_length=256, blank=True, null=True, default='N/A')
#     description = models.CharField(max_length=1000, blank=True, null=True, default='No description yet...')

#     country = models.CharField(max_length=50, default='Nigeria')
#     state = models.CharField(max_length=50) #, blank=True, null=True, default='Lagos')
#     lga = models.CharField(max_length=50) #, blank=True, null=True, default='N/A')
#     city = models.CharField(max_length=50, null=True, blank=True)
#     town = models.CharField(max_length=50, null=True, blank=True)
#     street = models.CharField(max_length=640)

#     SCHOOL_TYPE_CHOICE = (
#         ('c', 'Creche'),
#         ('n', 'Nursery'),
#         ('p', 'Primary'),
#         ('s', 'Secondary'),
#         ('al', 'A-Levels')
#     )

#     APPROVED_EXAM_CHOICE = (
#         ('ncce', 'National Common Entrance Examinations'),
#         ('scce', 'State Common Entrance Examinatins'),
#         ('waec', 'West African Examination Council Exams'),
#         ('neco', 'National Examinations Council Exams'),        
#         ('jwaec', 'Junior West African Examination Council Exams'),
#         ('jneco', 'Junior National Examinations Council Exams'),
#         ('toefl', 'TOEFL Exams'),
#         ('ielts', 'IELTS Exams'),
#         ('alevel', 'A-Levels Exams'),
#         ('igcse', 'IGCSE Exams')
#     )

#     GENDER_CHOICE = (
#         ('m', 'Male Only'),
#         ('f', 'Female Only'),
#         ('mx', 'Mixed')
#     )

#     BOARDING_CHOICE = (
#         ('fb', 'Full Boarding'),
#         ('fd', 'Day Only'),
#         ('bd', 'Day and Boarding')
#     )

#     approval_number = models.CharField(max_length=11, default='Awaiting')
#     admin = models.CharField(max_length=128, default='N/A')
#     school_type = MultiSelectField(choices=SCHOOL_TYPE_CHOICE, default='n') # max_choices not needed - use multi
#     approved_exams = MultiSelectField(choices=APPROVED_EXAM_CHOICE, default='ncce') # max_choices not needed - use multi
#     gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default='mx') # max_choices is 1 - use default
#     boarding = models.CharField(max_length=2, choices=BOARDING_CHOICE, default='bd') # max_choices is 1 - use default
#     founded = models.DateField(default='N/A')

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.school}'

# class AdvancedSchoolInfo(models.Model):
#     """Model representing a schools's advanced information."""
#     school = models.ForeignKey(School, on_delete=models.CASCADE)

#     ACTIVITY_CHOICE = (
#         ('carol', 'Creche'),
#         ('interhousesports', 'Interhouse Sports'),
#         ('culturalday', 'Cultural Day'),
#         ('dance', 'Dance'),
#         ('spellingbees', 'Spelling Bees'),
#         ('debate', 'Debate'),
#         ('quiz', 'Quiz'),        
#         ('swimming', 'Swimming'),
#         ('karate', 'Karate'),
#         ('costumeday', 'Costume Day')
#     )

#     CLUB_CHOICE = (
#         ('bscout', 'Boys Scout'),
#         ('gguide', 'Girls Guide'),
#         ('frsc', 'FRSC Club'),
#         ('music', 'Music Club'),        
#         ('drama', 'Drama Club'),
#         ('debate', 'Debate Club'),
#         ('press', 'Press Club'),
#         ('jets', 'JETS Club'),
#         ('rcross', 'Red Cross'),
#         ('artscraft', 'Arts-Craft Club')
#     )

#     FACILITY_CHOICE = (
#         ('sickbay', 'Sickbay'),
#         ('multipurposehall', 'Multipurpose Hall'),
#         ('sciencelab', 'Science Lab'),
#         ('busservice', 'Bus Service'),
#         ('library', 'Library'),
#         ('playground', 'Playground'),
#         ('sportscomplex', 'Sports Complex'),
#         ('ictcenter', 'ICT Center'),
#         ('artstudio', 'Art Studio'),
#         ('elibrary', 'E-Library'),
#         ('swimmingpool', 'Swimming Pool'),
#         ('orchard', 'Orchard'),
#         ('farmhouse', 'Farmhouse'),
#         ('specialneeds', 'Special Needs Care'),
#         ('musicstudio', 'Music Studio'),
#         ('stem', 'STEM'),
#         ('homemanagementlab', 'Home Management Lab'),
#         ('languagestudio', 'Language Studio')
#     )

#     activities = MultiSelectField(choices=ACTIVITY_CHOICE, default='debate')
#     clubs = MultiSelectField(choices=CLUB_CHOICE, default='debate')
#     facilities = MultiSelectField(choices=FACILITY_CHOICE, default='playground')

#     def __str__(self):
#         """String for representing the Model object."""
#         return f'{self.school}'

    
# class ContactUs(models.Model):
#     """Model representing contacting a schools."""
#     subject = models.CharField(max_length=100)
#     message = models.TextField()
#     sender = models.EmailField()
#     cc_myself = models.BooleanField()



class School(models.Model):
    """Model representing a school."""
    email = models.EmailField(_('School Email'), max_length=128)
    name = models.CharField(_('School Name'), max_length=128)
    phone = models.CharField(_('School Phone'), max_length=15)
    slug = models.SlugField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(SchoolsConnBaseUser, on_delete=models.CASCADE)

    # Basic Info 
    motto = models.CharField(max_length=256, blank=True, null=True, default='No Motto Available yet')
    description = models.CharField(max_length=1000, blank=True, null=True, default='No description yet...')

    country = models.CharField(max_length=50, default='Nigeria')
    state = models.CharField(max_length=50, default='Lagos') #, blank=True, null=True, default='Lagos')
    lga = models.CharField(_('LGA'), max_length=50, default='Ikeja') #, blank=True, null=True, default='N/A')
    city = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=640, default='N/A')

    # School Choice Region
    creche = models.BooleanField(default=False)
    nursery = models.BooleanField(default=False)
    primary = models.BooleanField(default=False)
    secondary = models.BooleanField(default=False)
    aLevels = models.BooleanField(_('A-Levels'), default=False)

    # Approved Exams Choice Region
    ncce = models.BooleanField(_('National Common Entrance'), default=False)
    scce = models.BooleanField(_('State Common Entrance'), default=False)
    waec = models.BooleanField(_('Senior WAEC Exams'), default=False)
    neco = models.BooleanField(_('Senior NECO Exams'), default=False)
    jwaec = models.BooleanField(_('Junior WAEC Exams'), default=False)
    jneco = models.BooleanField(_('Junior NECO Exams'), default=False)
    toefl = models.BooleanField(_('TOEFL Exams'), default=False)
    ielts = models.BooleanField(_('IELTS Exams'), default=False)
    alevel = models.BooleanField(_('A-Levels Exams'), default=False)
    igcse = models.BooleanField(_('IGCSE Exams'), default=False)

    GENDER_CHOICE = (
        ('m', 'Male Only'),
        ('f', 'Female Only'),
        ('mx', 'Mixed')
    )

    BOARDING_CHOICE = (
        ('fb', 'Full Boarding'),
        ('fd', 'Day Only'),
        ('bd', 'Day and Boarding')
    )

    approval_number = models.CharField(_('Govt Approval Number'), max_length=11, default='Awaiting')
    admin = models.CharField(_('Admission Officer'), max_length=128, default='N/A')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default='mx') # max_choices is 1 - use default
    boarding = models.CharField(max_length=2, choices=BOARDING_CHOICE, default='bd') # max_choices is 1 - use default
    founded = models.DateField(default=datetime.date.today)
    website = models.URLField(max_length=100, null=True, blank=True)

    # Advanced Info 
    # Activity Choice Region
    carol = models.BooleanField(default=False)
    interhousesports = models.BooleanField(_('Inter House Sports'), default=False)
    culturalday = models.BooleanField(_('Cultural Day'), default=False)
    dance = models.BooleanField(default=False)
    spellingbees = models.BooleanField(_('Spelling Bees'), default=False)
    debate = models.BooleanField(default=False)
    quiz = models.BooleanField(default=False)
    swimming = models.BooleanField(default=False)
    karate = models.BooleanField(default=False)
    costumeday = models.BooleanField(_('Costume Day'), default=False)

    # Clubs Choice Region
    gguide = models.BooleanField(_('Girl\'s Guide'), default=False)
    bscout = models.BooleanField(_('Boy\'s Scout'), default=False)
    frsc = models.BooleanField(_('FRSC'), default=False)
    music = models.BooleanField(default=False)
    drama = models.BooleanField(default=False)
    #debate = models.BooleanField(default=False)
    press = models.BooleanField(default=False)
    jets = models.BooleanField(_('JETs'), default=False)
    karate = models.BooleanField(default=False)
    rcross = models.BooleanField(_('Red Cross'), default=False)
    artscraft = models.BooleanField(_('Arts and Craft'), default=False)

    # Facility Choice Region
    sickbay = models.BooleanField(default=False)
    multipurposehall = models.BooleanField(_('Multipurpose Hall'), default=False)
    sciencelab = models.BooleanField(_('Science Lab'), default=False)
    busservice = models.BooleanField(_('Bus Service'), default=False)
    library = models.BooleanField(default=False)
    playground = models.BooleanField(default=False)
    sportscomplex = models.BooleanField(_('Sports Complex'), default=False)
    ictcenter = models.BooleanField(_('ICT Center'), default=False)
    artstudio = models.BooleanField(_('Art Studio'), default=False)
    #elibrary = models.BooleanField(_('E-Library'), default=False)
    orchard = models.BooleanField(_('Orchard'), default=False)
    farmhouse = models.BooleanField(_('Farm House'), default=False)
    specialneeds = models.BooleanField(_('Special Needs Care'), default=False)
    musicstudio = models.BooleanField(_('Music Studio'), default=False)
    #stem = models.BooleanField(_('STEM Labs'), default=False)
    homemanagementlab = models.BooleanField(_('Home Management Labs'), default=False)
    languagestudio = models.BooleanField(_('Languages Studio'), default=False)

    def get_absolute_url(self):
        """Returns the url to access a particular school instance."""
        # return reverse('tutor-detail', args=[str(self.email_address)])
        #return reverse('school-detail', args=[str(self.id)]) # school-detail is a view
        return reverse('school-detail', args=[str(self.slug)]) # school-detail is a view

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

    
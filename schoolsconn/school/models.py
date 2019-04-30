import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.urls import reverse
#from multiselectfield import MultiSelectField
from django.utils.translation import gettext as _

# https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/fields/#django.contrib.postgres.fields.ArrayField
# Note ArrayFields when using PostGress

def user_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'schools/user_{0}/{1}'.format(instance.user.id, filename)

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

class School(models.Model):
    """Model representing a school."""

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

    STATE_CHOICE = (
        (1, 'Abia'),
        (2, 'Adamawa'),
        (3, 'Akwa Ibom'),
        (4, 'Anambra'),
        (5, 'Bauchi'),
        (6, 'Bayelsa'),
        (7, 'Benue'),
        (8, 'Borno'),
        (9, 'Cross River'),
        (10, 'Delta'),
        (11, 'Ebonyi'),
        (12, 'Edo'),
        (13, 'Ekiti'),
        (14, 'Enugu'),
        (15, 'FCT'),
        (16, 'Gombe'),
        (17, 'Imo'),
        (18, 'Jigawa'),
        (19, 'Kaduna'),
        (20, 'Kano'),
        (21, 'Katsina'),
        (22, 'Kebbi'),
        (23, 'Kogi'),
        (24, 'Kwara'),
        (25, 'Lagos'),
        (26, 'Nasarawa'),
        (27, 'Niger'),
        (28, 'Ogun'),
        (29, 'Ondo'),
        (30, 'Osun'),
        (31, 'Oyo'),
        (32, 'Plateau'),
        (33, 'Rivers'),
        (34, 'Sokoto'),
        (35, 'Taraba'),
        (36, 'Yobe'),
        (37, 'Zamfara'),
    )

    email = models.EmailField(_('School Email'), max_length=128)
    name = models.CharField(_('School Name'), max_length=128)
    phone = models.CharField(_('School Phone'), max_length=15)
    motto = models.CharField(max_length=256)
    website = models.URLField(max_length=100, null=True, blank=True)

    slug = models.SlugField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(SchoolsConnBaseUser, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='schools/logo/', blank=True)

    # Basic Info 
    country = models.CharField(max_length=50, default='Nigeria')
    #state = models.CharField(max_length=50) #, blank=True, null=True, default='Lagos')
    state = models.CharField(max_length=2, choices=STATE_CHOICE)
    lga = models.CharField(_('LGA'), max_length=50) #, blank=True, null=True, default='N/A')
    #city = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50)
    street = models.CharField(max_length=640)
    
    approval_number = models.CharField(_('Govt Approval Number'), max_length=11, default='Awaiting')
    admin = models.CharField(_('Admission Officer'), max_length=128)
    founded = models.DateField(null=True, blank=True)

    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default='mx') # max_choices is 1 - use default
    boarding = models.CharField(max_length=2, choices=BOARDING_CHOICE, default='bd') # max_choices is 1 - use default
    description = models.CharField(max_length=1000)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


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

    verified = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Returns the url to access a particular school instance."""
        # return reverse('tutor-detail', args=[str(self.email_address)])
        #return reverse('school-detail', args=[str(self.id)]) # school-detail is a view
        return reverse('school-detail', args=[str(self.slug)]) # school-detail is a view

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'

class LGA(models.Model):
    ''' Model list of LGAs' in Nigeria '''
    LGA_CHOICE = (
        ('Abia_LGA', (
            (1, 'Aba North'),
            (2, 'Aba South'),
            (3, 'Arochukwu'),
            (4, 'Bende'),
            (5, 'Ikwuano'),
            (6, 'Isiala Ngwa North'),
            (7, 'Isiala Ngwa South'),
            (8, 'Isuikwuato'),
            (9, 'Obi Ngwa'),
            (10, 'Ohafia'),
            (11, 'Osisioma'),
            (12, 'Ugwunagbo'),
            (13, 'Ukwa East'),
            (14, 'Ukwa West'),
            (15, 'Umuahia North'),
            (16, 'Umuahia South'),
            (17, 'Umu Nneochi'),
        )),
        ('Adamawa_LGA', (
            (18, 'Demsa'),
            (19, 'Fufure'),
            (20, 'Ganye'),
            (21, 'Gayuk'),
            (22, 'Gombi'),
            (23, 'Grie'),
            (24, 'Hong'),
            (25, 'Jada'),
            (26, 'Larmurde'),
            (27, 'Madagali'),
            (28, 'Maiha'),
            (29, 'Mayo Belwa'),
            (30, 'Michika'),
            (31, 'Mubi North'),
            (32, 'Mubi South'),
            (33, 'Numan'),
            (34, 'Shelleng'),
            (35, 'Song'),
            (36, 'Toungo'),
            (37, 'Yola North'),
            (38, 'Yola South'),
        )),
        ('Akwa_Ibom_LGA', (
            (39, 'Abak'),
            (40, 'Eastern Obolo'),
            (41, 'Eket'),
            (42, 'Esit Eket'),
            (43, 'Essien Udim'),
            (44, 'Etim Ekpo'),
            (45, 'Etinan'),
            (46, 'Ibeno'),
            (47, 'Ibesikpo Asutan'),
            (48, 'Ibiono-Ibom'),
            (49, 'Ika'),
            (50, 'Ikono'),
            (51, 'Ikot Abasi'),
            (52, 'Ikot Ekpene'),
            (53, 'Ini'),
            (54, 'Itu'),
            (55, 'Mbo'),
            (56, 'Mkpat-Enin'),
            (57, 'Nsit-Atai'),
            (58, 'Nsit-Ibom'),
            (59, 'Nsit-Ubium'),
            (60, 'Obot Akara'),
            (61, 'Okobo'),
            (62, 'Onna'),
            (63, 'Oron'),
            (64, 'Oruk Anam'),
            (65, 'Udung-Uko'),
            (66, 'Ukanafun'),
            (67, 'Uruan'),
            (68, 'Urue-Offong/Oruko'),
            (69, 'Uyo'),
        )),
        ('Anambra_LGA', (
            (70, 'Aguata'),
            (71, 'Anambra East'),
            (72, 'Anambra West'),
            (73, 'Anaocha'),
            (74, 'Awka North'),
            (75, 'Awka South'),
            (76, 'Ayamelum'),
            (77, 'Dunukofia'),
            (78, 'Ekwusigo'),
            (79, 'Idemili North'),
            (80, 'Idemili South'),
            (81, 'Ihiala'),
            (82, 'Njikoka'),
            (83, 'Nnewi North'),
            (84, 'Nnewi South'),
            (85, 'Ogbaru'),
            (86, 'Onitsha North'),
            (87, 'Onitsha South'),
            (88, 'Orumba North'),
            (89, 'Orumba South'),
            (90, 'Oyi'),
        )),
        ('Bauchi_LGA', (
            (91, 'Alkaleri'),
            (92, 'Bauchi'),
            (93, 'Bogoro'),
            (94, 'Damban'),
            (95, 'Darazo'),
            (96, 'Dass'),
            (97, 'Gamawa'),
            (98, 'Ganjuwa'),
            (99, 'Giade'),
            (100, 'Itas/Gadau'),
            (101, 'Jama''are'),
            (102, 'Katagum'),
            (103, 'Kirfi'),
            (104, 'Misau'),
            (105, 'Ningi'),
            (106, 'Shira'),
            (107, 'Tafawa Balewa'),
            (108, 'Toro'),
            (109, 'Warji'),
            (110, 'Zaki'),
        )),
        ('Bayelsa_LGA', (
            (111, 'Brass'),
            (112, 'Ekeremor'),
            (113, 'Kolokuma/Opokuma'),
            (114, 'Nembe'),
            (115, 'Ogbia'),
            (116, 'Sagbama'),
            (117, 'Southern Ijaw'),
            (118, 'Yenagoa'),
        )),
        ('Benue_LGA', (
            (119, 'Agatu'),
            (120, 'Apa'),
            (121, 'Ado'),
            (122, 'Buruku'),
            (123, 'Gboko'),
            (124, 'Guma'),
            (125, 'Gwer East'),
            (126, 'Gwer West'),
            (127, 'Katsina-Ala'),
            (128, 'Konshisha'),
            (129, 'Kwande'),
            (130, 'Logo'),
            (131, 'Makurdi'),
            (132, 'Obi'),
            (133, 'Ogbadibo'),
            (134, 'Ohimini'),
            (135, 'Oju'),
            (136, 'Okpokwu'),
            (137, 'Oturkpo'),
            (138, 'Tarka'),
            (139, 'Ukum'),
            (140, 'Ushongo'),
            (141, 'Vandeikya'),
        )),
        ('Borno_LGA', (
            (142, 'Abadam'),
            (143, 'Askira/Uba'),
            (144, 'Bama'),
            (145, 'Bayo'),
            (146, 'Biu'),
            (147, 'Chibok'),
            (148, 'Damboa'),
            (149, 'Dikwa'),
            (150, 'Gubio'),
            (151, 'Guzamala'),
            (152, 'Gwoza'),
            (153, 'Hawul'),
            (154, 'Jere'),
            (155, 'Kaga'),
            (156, 'Kala/Balge'),
            (157, 'Konduga'),
            (158, 'Kukawa'),
            (159, 'Kwaya Kusar'),
            (160, 'Mafa'),
            (161, 'Magumeri'),
            (162, 'Maiduguri'),
            (163, 'Marte'),
            (164, 'Mobbar'),
            (165, 'Monguno'),
            (166, 'Ngala'),
            (167, 'Nganzai'),
            (168, 'Shani'),
        )),
        ('Cross_River_LGA', (
            (169, 'Abi'),
            (170, 'Akamkpa'),
            (171, 'Akpabuyo'),
            (172, 'Bakassi'),
            (173, 'Bekwarra'),
            (174, 'Biase'),
            (175, 'Boki'),
            (176, 'Calabar Municipal'),
            (177, 'Calabar South'),
            (178, 'Etung'),
            (179, 'Ikom'),
            (180, 'Obanliku'),
            (181, 'Obubra'),
            (182, 'Obudu'),
            (183, 'Odukpani'),
            (184, 'Ogoja'),
            (185, 'Yakuur'),
            (186, 'Yala'),
        )),
        ('Delta_LGA', (
            (187, 'Aniocha North'),
            (188, 'Aniocha South'),
            (189, 'Bomadi'),
            (190, 'Burutu'),
            (191, 'Ethiope East'),
            (192, 'Ethiope West'),
            (193, 'Ika North East'),
            (194, 'Ika South'),
            (195, 'Isoko North'),
            (196, 'Isoko South'),
            (197, 'Ndokwa East'),
            (198, 'Ndokwa West'),
            (199, 'Okpe'),
            (200, 'Oshimili North'),
            (201, 'Oshimili South'),
            (202, 'Patani'),
            (203, 'Sapele, Delta'),
            (204, 'Udu'),
            (205, 'Ughelli North'),
            (206, 'Ughelli South'),
            (207, 'Ukwuani'),
            (208, 'Uvwie'),
            (209, 'Warri North'),
            (210, 'Warri South'),
            (211, 'Warri South West'),
        )), 
        ('Ebonyi_LGA', (
            (212, 'Abakaliki'),
            (213, 'Afikpo North'),
            (214, 'Afikpo South'),
            (215, 'Ebonyi'),
            (216, 'Ezza North'),
            (217, 'Ezza South'),
            (218, 'Ikwo'),
            (219, 'Ishielu'),
            (220, 'Ivo'),
            (221, 'Izzi'),
            (222, 'Ohaozara'),
            (223, 'Ohaukwu'),
            (224, 'Onicha'),
        )), 
        ('Edo_LGA', (
            (225, 'Akoko-Edo'),
            (226, 'Egor'),
            (227, 'Esan Central'),
            (228, 'Esan North-East'),
            (229, 'Esan South-East'),
            (230, 'Esan West'),
            (231, 'Etsako Central'),
            (232, 'Etsako East'),
            (233, 'Etsako West'),
            (234, 'Igueben'),
            (235, 'Ikpoba Okha'),
            (236, 'Orhionmwon'),
            (237, 'Oredo'),
            (238, 'Ovia North-East'),
            (239, 'Ovia South-West'),
            (240, 'Owan East'),
            (241, 'Owan West'),
            (242, 'Uhunmwonde'),
        )), 
        ('Ekiti_LGA', (
            (243, 'Ado Ekiti'),
            (244, 'Efon'),
            (245, 'Ekiti East'),
            (246, 'Ekiti South-West'),
            (247, 'Ekiti West'),
            (248, 'Emure'),
            (249, 'Gbonyin'),
            (250, 'Ido Osi'),
            (251, 'Ijero'),
            (252, 'Ikere'),
            (253, 'Ikole'),
            (254, 'Ilejemeje'),
            (255, 'Irepodun/Ifelodun'),
            (256, 'Ise/Orun'),
            (257, 'Moba'),
            (258, 'Oye'),
        )), 
        ('Enugu_LGA', (
            (259, 'Aninri'),
            (260, 'Awgu'),
            (261, 'Enugu East'),
            (262, 'Enugu North'),
            (263, 'Enugu South'),
            (264, 'Ezeagu'),
            (265, 'Igbo Etiti'),
            (266, 'Igbo Eze North'),
            (267, 'Igbo Eze South'),
            (268, 'Isi Uzo'),
            (269, 'Nkanu East'),
            (270, 'Nkanu West'),
            (271, 'Nsukka'),
            (272, 'Oji River'),
            (273, 'Udenu'),
            (274, 'Udi'),
            (275, 'Uzo Uwani'),
        )), 
        ('FCT_LGA', (
            (276, 'Abaji'),
            (277, 'Bwari'),
            (278, 'Gwagwalada'),
            (279, 'Kuje'),
            (280, 'Kwali'),
            (281, 'Municipal Area Council'),
        )), 
        ('Gombe_LGA', (
            (282, 'Akko'),
            (283, 'Balanga'),
            (284, 'Billiri'),
            (285, 'Dukku'),
            (286, 'Funakaye'),
            (287, 'Gombe'),
            (288, 'Kaltungo'),
            (289, 'Kwami'),
            (290, 'Nafada'),
            (291, 'Shongom'),
            (292, 'Yamaltu/Deba'),
        )), 
        ('Imo_LGA', (
            (293, 'Aboh Mbaise'),
            (294, 'Ahiazu Mbaise'),
            (295, 'Ehime Mbano'),
            (296, 'Ezinihitte'),
            (297, 'Ideato North'),
            (298, 'Ideato South'),
            (299, 'Ihitte/Uboma'),
            (300, 'Ikeduru'),
            (301, 'Isiala Mbano'),
            (302, 'Isu'),
            (303, 'Mbaitoli'),
            (304, 'Ngor Okpala'),
            (305, 'Njaba'),
            (306, 'Nkwerre'),
            (307, 'Nwangele'),
            (308, 'Obowo'),
            (309, 'Oguta'),
            (310, 'Ohaji/Egbema'),
            (311, 'Okigwe'),
            (312, 'Orlu'),
            (313, 'Orsu'),
            (314, 'Oru East'),
            (315, 'Oru West'),
            (316, 'Owerri Municipal'),
            (317, 'Owerri North'),
            (318, 'Owerri West'),
            (319, 'Unuimo'),
        )), 
        ('Jigawa_LGA', (
            (320, 'Auyo'),
            (321, 'Babura'),
            (322, 'Biriniwa'),
            (323, 'Birnin Kudu'),
            (324, 'Buji'),
            (325, 'Dutse'),
            (326, 'Gagarawa'),
            (327, 'Garki'),
            (328, 'Gumel'),
            (329, 'Guri'),
            (330, 'Gwaram'),
            (331, 'Gwiwa'),
            (332, 'Hadejia'),
            (333, 'Jahun'),
            (334, 'Kafin Hausa'),
            (335, 'Kazaure'),
            (336, 'Kiri Kasama'),
            (337, 'Kiyawa'),
            (338, 'Kaugama'),
            (339, 'Maigatari'),
            (340, 'Malam Madori'),
            (341, 'Miga'),
            (342, 'Ringim'),
            (343, 'Roni'),
            (344, 'Sule Tankarkar'),
            (345, 'Taura'),
            (346, 'Yankwashi'),
        )), 
        ('Kaduna_LGA', (
            (347, 'Birnin Gwari'),
            (348, 'Chikun'),
            (349, 'Giwa'),
            (350, 'Igabi'),
            (351, 'Ikara'),
            (352, 'Jaba'),
            (353, 'Jema''a'),
            (354, 'Kachia'),
            (355, 'Kaduna North'),
            (356, 'Kaduna South'),
            (357, 'Kagarko'),
            (358, 'Kajuru'),
            (359, 'Kaura'),
            (360, 'Kauru'),
            (361, 'Kubau'),
            (362, 'Kudan'),
            (363, 'Lere'),
            (364, 'Makarfi'),
            (365, 'Sabon Gari'),
            (366, 'Sanga'),
            (367, 'Soba'),
            (368, 'Zangon Kataf'),
            (369, 'Zaria'),
        )),
        ('Kano_LGA', (
            (370, 'Ajingi'),
            (371, 'Albasu'),
            (372, 'Bagwai'),
            (373, 'Bebeji'),
            (374, 'Bichi'),
            (375, 'Bunkure'),
            (376, 'Dala'),
            (377, 'Dambatta'),
            (378, 'Dawakin Kudu'),
            (379, 'Dawakin Tofa'),
            (380, 'Doguwa'),
            (381, 'Fagge'),
            (382, 'Gabasawa'),
            (383, 'Garko'),
            (384, 'Garun Mallam'),
            (385, 'Gaya'),
            (386, 'Gezawa'),
            (387, 'Gwale'),
            (388, 'Gwarzo'),
            (389, 'Kabo'),
            (390, 'Kano Municipal'),
            (391, 'Karaye'),
            (392, 'Kibiya'),
            (393, 'Kiru'),
            (394, 'Kumbotso'),
            (395, 'Kunchi'),
            (396, 'Kura'),
            (397, 'Madobi'),
            (398, 'Makoda'),
            (399, 'Minjibir'),
            (400, 'Nasarawa'),
            (401, 'Rano'),
            (402, 'Rimin Gado'),
            (403, 'Rogo'),
            (404, 'Shanono'),
            (405, 'Sumaila'),
            (406, 'Takai'),
            (407, 'Tarauni'),
            (408, 'Tofa'),
            (409, 'Tsanyawa'),
            (410, 'Tudun Wada'),
            (411, 'Ungogo'),
            (412, 'Warawa'),
            (413, 'Wudil'),
        )),
        ('Katsina_LGA', (

        )),
        ('Kebbi_LGA', (

        )),
        ('Kogi_LGA', (

        )),
        ('Kwara_LGA', (

        )),
        ('Lagos_LGA', (

        )),
        ('Nasarawa_LGA', (

        )),
        ('Niger_LGA', (

        )),
        ('Ogun_LGA', (

        )),
        ('Ondo_LGA', (

        )),
        ('Osun_LGA', (

        )),
        ('Oyo_LGA', (

        )),
        ('Plateau_LGA', (

        )),
        ('Rivers_LGA', (

        )),
        ('Sokoto_LGA', (

        )),
        ('Taraba_LGA', (

        )),
        ('Yobe_LGA', (

        )),
        ('Zamfara_LGA', (

        )),


        (414, 'Bakori'),
        (415, 'Batagarawa'),
        (416, 'Batsari'),
        (417, 'Baure'),
        (418, 'Bindawa'),
        (419, 'Charanchi'),
        (420, 'Dandume'),
        (421, 'Danja'),
        (422, 'Dan Musa'),
        (423, 'Daura'),
        (424, 'Dutsi'),
        (425, 'Dutsin Ma'),
        (426, 'Faskari'),
        (427, 'Funtua'),
        (428, 'Ingawa'),
        (429, 'Jibia'),
        (430, 'Kafur'),
        (431, 'Kaita'),
        (432, 'Kankara'),
        (433, 'Kankia'),
        (434, 'Katsina'),
        (435, 'Kurfi'),
        (436, 'Kusada'),
        (437, 'Mai''Adua'),
        (438, 'Malumfashi'),
        (439, 'Mani'),
        (440, 'Mashi'),
        (441, 'Matazu'),
        (442, 'Musawa'),
        (443, 'Rimi'),
        (444, 'Sabuwa'),
        (445, 'Safana'),
        (446, 'Sandamu'),
        (447, 'Zango'),
        (448, 'Aleiro'),
        (449, 'Arewa Dandi'),
        (450, 'Argungu'),
        (451, 'Augie'),
        (452, 'Bagudo'),
        (453, 'Birnin Kebbi'),
        (454, 'Bunza'),
        (455, 'Dandi'),
        (456, 'Fakai'),
        (457, 'Gwandu'),
        (458, 'Jega'),
        (459, 'Kalgo'),
        (460, 'Koko/Besse'),
        (461, 'Maiyama'),
        (462, 'Ngaski'),
        (463, 'Sakaba'),
        (464, 'Shanga'),
        (465, 'Suru'),
        (466, 'Wasagu/Danko'),
        (467, 'Yauri'),
        (468, 'Zuru'),
        (469, 'Adavi'),
        (470, 'Ajaokuta'),
        (471, 'Ankpa'),
        (472, 'Bassa'),
        (473, 'Dekina'),
        (474, 'Ibaji'),
        (475, 'Idah'),
        (476, 'Igalamela Odolu'),
        (477, 'Ijumu'),
        (478, 'Kabba/Bunu'),
        (479, 'Kogi'),
        (480, 'Lokoja'),
        (481, 'Mopa Muro'),
        (482, 'Ofu'),
        (483, 'Ogori/Magongo'),
        (484, 'Okehi'),
        (485, 'Okene'),
        (486, 'Olamaboro'),
        (487, 'Omala'),
        (488, 'Yagba East'),
        (489, 'Yagba West'),
        (490, 'Asa'),
        (491, 'Baruten'),
        (492, 'Edu'),
        (493, 'Ekiti, Kwara State'),
        (494, 'Ifelodun'),
        (495, 'Ilorin East'),
        (496, 'Ilorin South'),
        (497, 'Ilorin West'),
        (498, 'Irepodun'),
        (499, 'Isin'),
        (500, 'Kaiama'),
        (501, 'Moro'),
        (502, 'Offa'),
        (503, 'Oke Ero'),
        (504, 'Oyun'),
        (505, 'Pategi'),
        (506, 'Agege'),
        (507, 'Ajeromi-Ifelodun'),
        (508, 'Alimosho'),
        (509, 'Amuwo-Odofin'),
        (510, 'Apapa'),
        (511, 'Badagry'),
        (512, 'Epe'),
        (513, 'Eti Osa'),
        (514, 'Ibeju-Lekki'),
        (515, 'Ifako-Ijaiye'),
        (516, 'Ikeja'),
        (517, 'Ikorodu'),
        (518, 'Kosofe'),
        (519, 'Lagos Island'),
        (520, 'Lagos Mainland'),
        (521, 'Mushin'),
        (522, 'Ojo'),
        (523, 'Oshodi-Isolo'),
        (524, 'Shomolu'),
        (525, 'Surulere, Lagos State'),
        (526, 'Akwanga'),
        (527, 'Awe'),
        (528, 'Doma'),
        (529, 'Karu'),
        (530, 'Keana'),
        (531, 'Keffi'),
        (532, 'Kokona'),
        (533, 'Lafia'),
        (534, 'Nasarawa'),
        (535, 'Nasarawa Egon'),
        (536, 'Obi'),
        (537, 'Toto'),
        (538, 'Wamba'),
        (539, 'Agaie'),
        (540, 'Agwara'),
        (541, 'Bida'),
        (542, 'Borgu'),
        (543, 'Bosso'),
        (544, 'Chanchaga'),
        (545, 'Edati'),
        (546, 'Gbako'),
        (547, 'Gurara'),
        (548, 'Katcha'),
        (549, 'Kontagora'),
        (550, 'Lapai'),
        (551, 'Lavun'),
        (552, 'Magama'),
        (553, 'Mariga'),
        (554, 'Mashegu'),
        (555, 'Mokwa'),
        (556, 'Moya'),
        (557, 'Paikoro'),
        (558, 'Rafi'),
        (559, 'Rijau'),
        (560, 'Shiroro'),
        (561, 'Suleja'),
        (562, 'Tafa'),
        (563, 'Wushishi'),
        (564, 'Abeokuta North'),
        (565, 'Abeokuta South'),
        (566, 'Ado-Odo/Ota'),
        (567, 'Egbado North'),
        (568, 'Egbado South'),
        (569, 'Ewekoro'),
        (570, 'Ifo'),
        (571, 'Ijebu East'),
        (572, 'Ijebu North'),
        (573, 'Ijebu North East'),
        (574, 'Ijebu Ode'),
        (575, 'Ikenne'),
        (576, 'Imeko Afon'),
        (577, 'Ipokia'),
        (578, 'Obafemi Owode'),
        (579, 'Odeda'),
        (580, 'Odogbolu'),
        (581, 'Ogun Waterside'),
        (582, 'Remo North'),
        (583, 'Shagamu'),
        (584, 'Akoko North-East'),
        (585, 'Akoko North-West'),
        (586, 'Akoko South-West'),
        (587, 'Akoko South-East'),
        (588, 'Akure North'),
        (589, 'Akure South'),
        (590, 'Ese Odo'),
        (591, 'Idanre'),
        (592, 'Ifedore'),
        (593, 'Ilaje'),
        (594, 'Ile Oluji/Okeigbo'),
        (595, 'Irele'),
        (596, 'Odigbo'),
        (597, 'Okitipupa'),
        (598, 'Ondo East'),
        (599, 'Ondo West'),
        (600, 'Ose'),
        (601, 'Owo'),
        (602, 'Atakunmosa East'),
        (603, 'Atakunmosa West'),
        (604, 'Aiyedaade'),
        (605, 'Aiyedire'),
        (606, 'Boluwaduro'),
        (607, 'Boripe'),
        (608, 'Ede North'),
        (609, 'Ede South'),
        (610, 'Ife Central'),
        (611, 'Ife East'),
        (612, 'Ife North'),
        (613, 'Ife South'),
        (614, 'Egbedore'),
        (615, 'Ejigbo'),
        (616, 'Ifedayo'),
        (617, 'Ifelodun'),
        (618, 'Ila'),
        (619, 'Ilesa East'),
        (620, 'Ilesa West'),
        (621, 'Irepodun'),
        (622, 'Irewole'),
        (623, 'Isokan'),
        (624, 'Iwo'),
        (625, 'Obokun'),
        (626, 'Odo Otin'),
        (627, 'Ola Oluwa'),
        (628, 'Olorunda'),
        (629, 'Oriade'),
        (630, 'Orolu'),
        (631, 'Osogbo'),
        (632, 'Afijio'),
        (633, 'Akinyele'),
        (634, 'Atiba'),
        (635, 'Atisbo'),
        (636, 'Egbeda'),
        (637, 'Ibadan North'),
        (638, 'Ibadan North-East'),
        (639, 'Ibadan North-West'),
        (640, 'Ibadan South-East'),
        (641, 'Ibadan South-West'),
        (642, 'Ibarapa Central'),
        (643, 'Ibarapa East'),
        (644, 'Ibarapa North'),
        (645, 'Ido'),
        (646, 'Irepo'),
        (647, 'Iseyin'),
        (648, 'Itesiwaju'),
        (649, 'Iwajowa'),
        (650, 'Kajola'),
        (651, 'Lagelu'),
        (652, 'Ogbomosho North'),
        (653, 'Ogbomosho South'),
        (654, 'Ogo Oluwa'),
        (655, 'Olorunsogo'),
        (656, 'Oluyole'),
        (657, 'Ona Ara'),
        (658, 'Orelope'),
        (659, 'Ori Ire'),
        (660, 'Oyo'),
        (661, 'Oyo East'),
        (662, 'Saki East'),
        (663, 'Saki West'),
        (664, 'Surulere, Oyo State'),
        (665, 'Bokkos'),
        (666, 'Barkin Ladi'),
        (667, 'Bassa'),
        (668, 'Jos East'),
        (669, 'Jos North'),
        (670, 'Jos South'),
        (671, 'Kanam'),
        (672, 'Kanke'),
        (673, 'Langtang South'),
        (674, 'Langtang North'),
        (675, 'Mangu'),
        (676, 'Mikang'),
        (677, 'Pankshin'),
        (678, 'Qua''an Pan'),
        (679, 'Riyom'),
        (680, 'Shendam'),
        (681, 'Wase'),
        (682, 'Abua/Odual'),
        (683, 'Ahoada East'),
        (684, 'Ahoada West'),
        (685, 'Akuku-Toru'),
        (686, 'Andoni'),
        (687, 'Asari-Toru'),
        (688, 'Bonny'),
        (689, 'Degema'),
        (690, 'Eleme'),
        (691, 'Emuoha'),
        (692, 'Etche'),
        (693, 'Gokana'),
        (694, 'Ikwerre'),
        (695, 'Khana'),
        (696, 'Obio/Akpor'),
        (697, 'Ogba/Egbema/Ndoni'),
        (698, 'Ogu/Bolo'),
        (699, 'Okrika'),
        (700, 'Omuma'),
        (701, 'Opobo/Nkoro'),
        (702, 'Oyigbo'),
        (703, 'Port Harcourt'),
        (704, 'Tai'),
        (705, 'Binji'),
        (706, 'Bodinga'),
        (707, 'Dange Shuni'),
        (708, 'Gada'),
        (709, 'Goronyo'),
        (710, 'Gudu'),
        (711, 'Gwadabawa'),
        (712, 'Illela'),
        (713, 'Isa'),
        (714, 'Kebbe'),
        (715, 'Kware'),
        (716, 'Rabah'),
        (717, 'Sabon Birni'),
        (718, 'Shagari'),
        (719, 'Silame'),
        (720, 'Sokoto North'),
        (721, 'Sokoto South'),
        (722, 'Tambuwal'),
        (723, 'Tangaza'),
        (724, 'Tureta'),
        (725, 'Wamako'),
        (726, 'Wurno'),
        (727, 'Yabo'),
        (728, 'Ardo Kola'),
        (729, 'Bali'),
        (730, 'Donga'),
        (731, 'Gashaka'),
        (732, 'Gassol'),
        (733, 'Ibi'),
        (734, 'Jalingo'),
        (735, 'Karim Lamido'),
        (736, 'Kumi'),
        (737, 'Lau'),
        (738, 'Sardauna'),
        (739, 'Takum'),
        (740, 'Ussa'),
        (741, 'Wukari'),
        (742, 'Yorro'),
        (743, 'Zing'),
        (744, 'Bade'),
        (745, 'Bursari'),
        (746, 'Damaturu'),
        (747, 'Fika'),
        (748, 'Fune'),
        (749, 'Geidam'),
        (750, 'Gujba'),
        (751, 'Gulani'),
        (752, 'Jakusko'),
        (753, 'Karasuwa'),
        (754, 'Machina'),
        (755, 'Nangere'),
        (756, 'Nguru'),
        (757, 'Potiskum'),
        (758, 'Tarmuwa'),
        (759, 'Yunusari'),
        (760, 'Yusufari'),
        (761, 'Anka'),
        (762, 'Bakura'),
        (763, 'Birnin Magaji/Kiyaw'),
        (764, 'Bukkuyum'),
        (765, 'Bungudu'),
        (766, 'Gummi'),
        (767, 'Gusau'),
        (768, 'Kaura Namoda'),
        (769, 'Maradun'),
        (770, 'Maru'),
        (771, 'Shinkafi'),
        (772, 'Talata Mafara'),
        (773, 'Chafe'),
        (774, 'Zurmi'),
    )
    lga = models.CharField(_('LGA'), max_length=3, choices=LGA_CHOICE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'schools/user_{0}/{1}'.format(instance.user.id, filename)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='schools/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
            
class DocumentMultiple(models.Model):
    desc_multiple = models.CharField(max_length=255, blank=True)
    doc_multiple = models.ImageField(upload_to='schools/multiple/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
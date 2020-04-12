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

class UserMessage(models.Model):
    pass

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
        ('Abia', 'Abia'),
        ('Adamawa', 'Adamawa'),
        ('Akwa Ibom', 'Akwa Ibom'),
        ('Anambra', 'Anambra'),
        ('Bauchi', 'Bauchi'),
        ('Bayelsa', 'Bayelsa'),
        ('Benue', 'Benue'),
        ('Borno', 'Borno'),
        ('Cross River', 'Cross River'),
        ('Delta', 'Delta'),
        ('Ebonyi', 'Ebonyi'),
        ('Edo', 'Edo'),
        ('Ekiti', 'Ekiti'),
        ('Enugu', 'Enugu'),
        ('FCT', 'FCT'),
        ('Gombe', 'Gombe'),
        ('Imo', 'Imo'),
        ('Jigawa', 'Jigawa'),
        ('Kaduna', 'Kaduna'),
        ('Kano', 'Kano'),
        ('Katsina', 'Katsina'),
        ('Kebbi', 'Kebbi'),
        ('Kogi', 'Kogi'),
        ('Kwara', 'Kwara'),
        ('Lagos', 'Lagos'),
        ('Nasarawa', 'Nasarawa'),
        ('Niger', 'Niger'),
        ('Ogun', 'Ogun'),
        ('Ondo', 'Ondo'),
        ('Osun', 'Osun'),
        ('Oyo', 'Oyo'),
        ('Plateau', 'Plateau'),
        ('Rivers', 'Rivers'),
        ('Sokoto', 'Sokoto'),
        ('Taraba', 'Taraba'),
        ('Yobe', 'Yobe'),
        ('Zamfara', 'Zamfara'),
        (None, 'Select a State'),
    )

    LGA_CHOICE = (
        ('Abia LGA', (
            ('Aba North', 'Aba North'),
            ('Aba South', 'Aba South'),
            ('Arochukwu', 'Arochukwu'),
            ('Bende', 'Bende'),
            ('Ikwuano', 'Ikwuano'),
            ('Isiala Ngwa North', 'Isiala Ngwa North'),
            ('Isiala Ngwa South', 'Isiala Ngwa South'),
            ('Isuikwuato', 'Isuikwuato'),
            ('Obi Ngwa', 'Obi Ngwa'),
            ('Ohafia', 'Ohafia'),
            ('Osisioma', 'Osisioma'),
            ('Ugwunagbo', 'Ugwunagbo'),
            ('Ukwa East', 'Ukwa East'),
            ('Ukwa West', 'Ukwa West'),
            ('Umuahia North', 'Umuahia North'),
            ('Umuahia South', 'Umuahia South'),
            ('Umu Nneochi', 'Umu Nneochi'),
        )),
        ('Adamawa LGA', (
            ('Demsa', 'Demsa'),
            ('Fufure', 'Fufure'),
            ('Ganye', 'Ganye'),
            ('Gayuk', 'Gayuk'),
            ('Gombi', 'Gombi'),
            ('Grie', 'Grie'),
            ('Hong', 'Hong'),
            ('Jada', 'Jada'),
            ('Larmurde', 'Larmurde'),
            ('Madagali', 'Madagali'),
            ('Maiha', 'Maiha'),
            ('Mayo Belwa', 'Mayo Belwa'),
            ('Michika', 'Michika'),
            ('Mubi North', 'Mubi North'),
            ('Mubi South', 'Mubi South'),
            ('Numan', 'Numan'),
            ('Shelleng', 'Shelleng'),
            ('Song', 'Song'),
            ('Toungo', 'Toungo'),
            ('Yola North', 'Yola North'),
            ('Yola South', 'Yola South'),
        )),
        ('Akwa Ibom LGA', (
            ('Abak', 'Abak'),
            ('Eastern Obolo', 'Eastern Obolo'),
            ('Eket', 'Eket'),
            ('Esit Eket', 'Esit Eket'),
            ('Essien Udim', 'Essien Udim'),
            ('Etim Ekpo', 'Etim Ekpo'),
            ('Etinan', 'Etinan'),
            ('Ibeno', 'Ibeno'),
            ('Ibesikpo Asutan', 'Ibesikpo Asutan'),
            ('Ibiono-Ibom', 'Ibiono-Ibom'),
            ('Ika', 'Ika'),
            ('Ikono', 'Ikono'),
            ('Ikot Abasi', 'Ikot Abasi'),
            ('Ikot Ekpene', 'Ikot Ekpene'),
            ('Ini', 'Ini'),
            ('Itu', 'Itu'),
            ('Mbo', 'Mbo'),
            ('Mkpat-Enin', 'Mkpat-Enin'),
            ('Nsit-Atai', 'Nsit-Atai'),
            ('Nsit-Ibom', 'Nsit-Ibom'),
            ('Nsit-Ubium', 'Nsit-Ubium'),
            ('Obot Akara', 'Obot Akara'),
            ('Okobo', 'Okobo'),
            ('Onna', 'Onna'),
            ('Oron', 'Oron'),
            ('Oruk Anam', 'Oruk Anam'),
            ('Udung-Uko', 'Udung-Uko'),
            ('Ukanafun', 'Ukanafun'),
            ('Uruan', 'Uruan'),
            ('Urue-Offong-Oruko', 'Urue-Offong-Oruko'),
            ('Uyo', 'Uyo'),
        )),
        ('Anambra LGA', (
            ('Aguata', 'Aguata'),
            ('Anambra East', 'Anambra East'),
            ('Anambra West', 'Anambra West'),
            ('Anaocha', 'Anaocha'),
            ('Awka North', 'Awka North'),
            ('Awka South', 'Awka South'),
            ('Ayamelum', 'Ayamelum'),
            ('Dunukofia', 'Dunukofia'),
            ('Ekwusigo', 'Ekwusigo'),
            ('Idemili North', 'Idemili North'),
            ('Idemili South', 'Idemili South'),
            ('Ihiala', 'Ihiala'),
            ('Njikoka', 'Njikoka'),
            ('Nnewi North', 'Nnewi North'),
            ('Nnewi South', 'Nnewi South'),
            ('Ogbaru', 'Ogbaru'),
            ('Onitsha North', 'Onitsha North'),
            ('Onitsha South', 'Onitsha South'),
            ('Orumba North', 'Orumba North'),
            ('Orumba South', 'Orumba South'),
            ('Oyi', 'Oyi'),
        )),
        ('Bauchi LGA', (
            ('Alkaleri', 'Alkaleri'),
            ('Bauchi', 'Bauchi'),
            ('Bogoro', 'Bogoro'),
            ('Damban', 'Damban'),
            ('Darazo', 'Darazo'),
            ('Dass', 'Dass'),
            ('Gamawa', 'Gamawa'),
            ('Ganjuwa', 'Ganjuwa'),
            ('Giade', 'Giade'),
            ('Itas-Gadau', 'Itas-Gadau'),
            ('Jamaare', 'Jamaare'),
            ('Katagum', 'Katagum'),
            ('Kirfi', 'Kirfi'),
            ('Misau', 'Misau'),
            ('Ningi', 'Ningi'),
            ('Shira', 'Shira'),
            ('Tafawa Balewa', 'Tafawa Balewa'),
            ('Toro', 'Toro'),
            ('Warji', 'Warji'),
            ('Zaki', 'Zaki'),
        )),
        ('Bayelsa LGA', (
            ('Brass', 'Brass'),
            ('Ekeremor', 'Ekeremor'),
            ('Kolokuma-Opokuma', 'Kolokuma-Opokuma'),
            ('Nembe', 'Nembe'),
            ('Ogbia', 'Ogbia'),
            ('Sagbama', 'Sagbama'),
            ('Southern Ijaw', 'Southern Ijaw'),
            ('Yenagoa', 'Yenagoa'),
        )),
        ('Benue LGA', (
            ('Agatu', 'Agatu'),
            ('Apa', 'Apa'),
            ('Ado', 'Ado'),
            ('Buruku', 'Buruku'),
            ('Gboko', 'Gboko'),
            ('Guma', 'Guma'),
            ('Gwer East', 'Gwer East'),
            ('Gwer West', 'Gwer West'),
            ('Katsina-Ala', 'Katsina-Ala'),
            ('Konshisha', 'Konshisha'),
            ('Kwande', 'Kwande'),
            ('Logo', 'Logo'),
            ('Makurdi', 'Makurdi'),
            ('Obi', 'Obi'),
            ('Ogbadibo', 'Ogbadibo'),
            ('Ohimini', 'Ohimini'),
            ('Oju', 'Oju'),
            ('Okpokwu', 'Okpokwu'),
            ('Oturkpo', 'Oturkpo'),
            ('Tarka', 'Tarka'),
            ('Ukum', 'Ukum'),
            ('Ushongo', 'Ushongo'),
            ('Vandeikya', 'Vandeikya'),
        )),
        ('Borno LGA', (
            ('Abadam', 'Abadam'),
            ('Askira-Uba', 'Askira-Uba'),
            ('Bama', 'Bama'),
            ('Bayo', 'Bayo'),
            ('Biu', 'Biu'),
            ('Chibok', 'Chibok'),
            ('Damboa', 'Damboa'),
            ('Dikwa', 'Dikwa'),
            ('Gubio', 'Gubio'),
            ('Guzamala', 'Guzamala'),
            ('Gwoza', 'Gwoza'),
            ('Hawul', 'Hawul'),
            ('Jere', 'Jere'),
            ('Kaga', 'Kaga'),
            ('Kala-Balge', 'Kala-Balge'),
            ('Konduga', 'Konduga'),
            ('Kukawa', 'Kukawa'),
            ('Kwaya Kusar', 'Kwaya Kusar'),
            ('Mafa', 'Mafa'),
            ('Magumeri', 'Magumeri'),
            ('Maiduguri', 'Maiduguri'),
            ('Marte', 'Marte'),
            ('Mobbar', 'Mobbar'),
            ('Monguno', 'Monguno'),
            ('Ngala', 'Ngala'),
            ('Nganzai', 'Nganzai'),
            ('Shani', 'Shani'),
        )),
        ('Cross River LGA', (
            ('Abi', 'Abi'),
            ('Akamkpa', 'Akamkpa'),
            ('Akpabuyo', 'Akpabuyo'),
            ('Bakassi', 'Bakassi'),
            ('Bekwarra', 'Bekwarra'),
            ('Biase', 'Biase'),
            ('Boki', 'Boki'),
            ('Calabar Municipal', 'Calabar Municipal'),
            ('Calabar South', 'Calabar South'),
            ('Etung', 'Etung'),
            ('Ikom', 'Ikom'),
            ('Obanliku', 'Obanliku'),
            ('Obubra', 'Obubra'),
            ('Obudu', 'Obudu'),
            ('Odukpani', 'Odukpani'),
            ('Ogoja', 'Ogoja'),
            ('Yakuur', 'Yakuur'),
            ('Yala', 'Yala'),
        )),
        ('Delta LGA', (
            ('Aniocha North', 'Aniocha North'),
            ('Aniocha South', 'Aniocha South'),
            ('Bomadi', 'Bomadi'),
            ('Burutu', 'Burutu'),
            ('Ethiope East', 'Ethiope East'),
            ('Ethiope West', 'Ethiope West'),
            ('Ika North East', 'Ika North East'),
            ('Ika South', 'Ika South'),
            ('Isoko North', 'Isoko North'),
            ('Isoko South', 'Isoko South'),
            ('Ndokwa East', 'Ndokwa East'),
            ('Ndokwa West', 'Ndokwa West'),
            ('Okpe', 'Okpe'),
            ('Oshimili North', 'Oshimili North'),
            ('Oshimili South', 'Oshimili South'),
            ('Patani', 'Patani'),
            ('Sapele-Delta', 'Sapele-Delta'),
            ('Udu', 'Udu'),
            ('Ughelli North', 'Ughelli North'),
            ('Ughelli South', 'Ughelli South'),
            ('Ukwuani', 'Ukwuani'),
            ('Uvwie', 'Uvwie'),
            ('Warri North', 'Warri North'),
            ('Warri South', 'Warri South'),
            ('Warri South West', 'Warri South West'),
        )), 
        ('Ebonyi LGA', (
            ('Abakaliki', 'Abakaliki'),
            ('Afikpo North', 'Afikpo North'),
            ('Afikpo South', 'Afikpo South'),
            ('Ebonyi', 'Ebonyi'),
            ('Ezza North', 'Ezza North'),
            ('Ezza South', 'Ezza South'),
            ('Ikwo', 'Ikwo'),
            ('Ishielu', 'Ishielu'),
            ('Ivo', 'Ivo'),
            ('Izzi', 'Izzi'),
            ('Ohaozara', 'Ohaozara'),
            ('Ohaukwu', 'Ohaukwu'),
            ('Onicha', 'Onicha'),
        )), 
        ('Edo LGA', (
            ('Akoko-Edo', 'Akoko-Edo'),
            ('Egor', 'Egor'),
            ('Esan Central', 'Esan Central'),
            ('Esan North-East', 'Esan North-East'),
            ('Esan South-East', 'Esan South-East'),
            ('Esan West', 'Esan West'),
            ('Etsako Central', 'Etsako Central'),
            ('Etsako East', 'Etsako East'),
            ('Etsako West', 'Etsako West'),
            ('Igueben', 'Igueben'),
            ('Ikpoba Okha', 'Ikpoba Okha'),
            ('Orhionmwon', 'Orhionmwon'),
            ('Oredo', 'Oredo'),
            ('Ovia North-East', 'Ovia North-East'),
            ('Ovia South-West', 'Ovia South-West'),
            ('Owan East', 'Owan East'),
            ('Owan West', 'Owan West'),
            ('Uhunmwonde', 'Uhunmwonde'),
        )), 
        ('Ekiti LGA', (
            ('Ado Ekiti', 'Ado Ekiti'),
            ('Efon', 'Efon'),
            ('Ekiti East', 'Ekiti East'),
            ('Ekiti South-West', 'Ekiti South-West'),
            ('Ekiti West', 'Ekiti West'),
            ('Emure', 'Emure'),
            ('Gbonyin', 'Gbonyin'),
            ('Ido Osi', 'Ido Osi'),
            ('Ijero', 'Ijero'),
            ('Ikere', 'Ikere'),
            ('Ikole', 'Ikole'),
            ('Ilejemeje', 'Ilejemeje'),
            ('Irepodun-Ifelodun', 'Irepodun-Ifelodun'),
            ('Ise-Orun', 'Ise-Orun'),
            ('Moba', 'Moba'),
            ('Oye', 'Oye'),
        )), 
        ('Enugu LGA', (
            ('Aninri', 'Aninri'),
            ('Awgu', 'Awgu'),
            ('Enugu East', 'Enugu East'),
            ('Enugu North', 'Enugu North'),
            ('Enugu South', 'Enugu South'),
            ('Ezeagu', 'Ezeagu'),
            ('Igbo Etiti', 'Igbo Etiti'),
            ('Igbo Eze North', 'Igbo Eze North'),
            ('Igbo Eze South', 'Igbo Eze South'),
            ('Isi Uzo', 'Isi Uzo'),
            ('Nkanu East', 'Nkanu East'),
            ('Nkanu West', 'Nkanu West'),
            ('Nsukka', 'Nsukka'),
            ('Oji River', 'Oji River'),
            ('Udenu', 'Udenu'),
            ('Udi', 'Udi'),
            ('Uzo Uwani', 'Uzo Uwani'),
        )), 
        ('FCT LGA', (
            ('Abaji', 'Abaji'),
            ('Bwari', 'Bwari'),
            ('Gwagwalada', 'Gwagwalada'),
            ('Kuje', 'Kuje'),
            ('Kwali', 'Kwali'),
            ('Municipal Area Council', 'Municipal Area Council'),
        )), 
        ('Gombe LGA', (
            ('Akko', 'Akko'),
            ('Balanga', 'Balanga'),
            ('Billiri', 'Billiri'),
            ('Dukku', 'Dukku'),
            ('Funakaye', 'Funakaye'),
            ('Gombe', 'Gombe'),
            ('Kaltungo', 'Kaltungo'),
            ('Kwami', 'Kwami'),
            ('Nafada', 'Nafada'),
            ('Shongom', 'Shongom'),
            ('Yamaltu-Deba', 'Yamaltu-Deba'),
        )), 
        ('Imo LGA', (
            ('Aboh Mbaise', 'Aboh Mbaise'),
            ('Ahiazu Mbaise', 'Ahiazu Mbaise'),
            ('Ehime Mbano', 'Ehime Mbano'),
            ('Ezinihitte', 'Ezinihitte'),
            ('Ideato North', 'Ideato North'),
            ('Ideato South', 'Ideato South'),
            ('Ihitte-Uboma', 'Ihitte-Uboma'),
            ('Ikeduru', 'Ikeduru'),
            ('Isiala Mbano', 'Isiala Mbano'),
            ('Isu', 'Isu'),
            ('Mbaitoli', 'Mbaitoli'),
            ('Ngor Okpala', 'Ngor Okpala'),
            ('Njaba', 'Njaba'),
            ('Nkwerre', 'Nkwerre'),
            ('Nwangele', 'Nwangele'),
            ('Obowo', 'Obowo'),
            ('Oguta', 'Oguta'),
            ('Ohaji-Egbema', 'Ohaji-Egbema'),
            ('Okigwe', 'Okigwe'),
            ('Orlu', 'Orlu'),
            ('Orsu', 'Orsu'),
            ('Oru East', 'Oru East'),
            ('Oru West', 'Oru West'),
            ('Owerri Municipal', 'Owerri Municipal'),
            ('Owerri North', 'Owerri North'),
            ('Owerri West', 'Owerri West'),
            ('Unuimo', 'Unuimo'),
        )), 
        ('Jigawa LGA', (
            ('Auyo', 'Auyo'),
            ('Babura', 'Babura'),
            ('Biriniwa', 'Biriniwa'),
            ('Birnin Kudu', 'Birnin Kudu'),
            ('Buji', 'Buji'),
            ('Dutse', 'Dutse'),
            ('Gagarawa', 'Gagarawa'),
            ('Garki', 'Garki'),
            ('Gumel', 'Gumel'),
            ('Guri', 'Guri'),
            ('Gwaram', 'Gwaram'),
            ('Gwiwa', 'Gwiwa'),
            ('Hadejia', 'Hadejia'),
            ('Jahun', 'Jahun'),
            ('Kafin Hausa', 'Kafin Hausa'),
            ('Kazaure', 'Kazaure'),
            ('Kiri Kasama', 'Kiri Kasama'),
            ('Kiyawa', 'Kiyawa'),
            ('Kaugama', 'Kaugama'),
            ('Maigatari', 'Maigatari'),
            ('Malam Madori', 'Malam Madori'),
            ('Miga', 'Miga'),
            ('Ringim', 'Ringim'),
            ('Roni', 'Roni'),
            ('Sule Tankarkar', 'Sule Tankarkar'),
            ('Taura', 'Taura'),
            ('Yankwashi', 'Yankwashi'),
        )), 
        ('Kaduna LGA', (
            ('Birnin Gwari', 'Birnin Gwari'),
            ('Chikun', 'Chikun'),
            ('Giwa', 'Giwa'),
            ('Igabi', 'Igabi'),
            ('Ikara', 'Ikara'),
            ('Jaba', 'Jaba'),
            ('Jema''a', 'Jema''a'),
            ('Kachia', 'Kachia'),
            ('Kaduna North', 'Kaduna North'),
            ('Kaduna South', 'Kaduna South'),
            ('Kagarko', 'Kagarko'),
            ('Kajuru', 'Kajuru'),
            ('Kaura', 'Kaura'),
            ('Kauru', 'Kauru'),
            ('Kubau', 'Kubau'),
            ('Kudan', 'Kudan'),
            ('Lere', 'Lere'),
            ('Makarfi', 'Makarfi'),
            ('Sabon Gari', 'Sabon Gari'),
            ('Sanga', 'Sanga'),
            ('Soba', 'Soba'),
            ('Zangon Kataf', 'Zangon Kataf'),
            ('Zaria', 'Zaria'),
        )),
        ('Kano LGA', (
            ('Ajingi', 'Ajingi'),
            ('Albasu', 'Albasu'),
            ('Bagwai', 'Bagwai'),
            ('Bebeji', 'Bebeji'),
            ('Bichi', 'Bichi'),
            ('Bunkure', 'Bunkure'),
            ('Dala', 'Dala'),
            ('Dambatta', 'Dambatta'),
            ('Dawakin Kudu', 'Dawakin Kudu'),
            ('Dawakin Tofa', 'Dawakin Tofa'),
            ('Doguwa', 'Doguwa'),
            ('Fagge', 'Fagge'),
            ('Gabasawa', 'Gabasawa'),
            ('Garko', 'Garko'),
            ('Garun Mallam', 'Garun Mallam'),
            ('Gaya', 'Gaya'),
            ('Gezawa', 'Gezawa'),
            ('Gwale', 'Gwale'),
            ('Gwarzo', 'Gwarzo'),
            ('Kabo', 'Kabo'),
            ('Kano Municipal', 'Kano Municipal'),
            ('Karaye', 'Karaye'),
            ('Kibiya', 'Kibiya'),
            ('Kiru', 'Kiru'),
            ('Kumbotso', 'Kumbotso'),
            ('Kunchi', 'Kunchi'),
            ('Kura', 'Kura'),
            ('Madobi', 'Madobi'),
            ('Makoda', 'Makoda'),
            ('Minjibir', 'Minjibir'),
            ('Nasarawa', 'Nasarawa'),
            ('Rano', 'Rano'),
            ('Rimin Gado', 'Rimin Gado'),
            ('Rogo', 'Rogo'),
            ('Shanono', 'Shanono'),
            ('Sumaila', 'Sumaila'),
            ('Takai', 'Takai'),
            ('Tarauni', 'Tarauni'),
            ('Tofa', 'Tofa'),
            ('Tsanyawa', 'Tsanyawa'),
            ('Tudun Wada', 'Tudun Wada'),
            ('Ungogo', 'Ungogo'),
            ('Warawa', 'Warawa'),
            ('Wudil', 'Wudil'),
        )),
        ('Katsina LGA', (
            ('Bakori', 'Bakori'),
            ('Batagarawa', 'Batagarawa'),
            ('Batsari', 'Batsari'),
            ('Baure', 'Baure'),
            ('Bindawa', 'Bindawa'),
            ('Charanchi', 'Charanchi'),
            ('Dandume', 'Dandume'),
            ('Danja', 'Danja'),
            ('Dan Musa', 'Dan Musa'),
            ('Daura', 'Daura'),
            ('Dutsi', 'Dutsi'),
            ('Dutsin Ma', 'Dutsin Ma'),
            ('Faskari', 'Faskari'),
            ('Funtua', 'Funtua'),
            ('Ingawa', 'Ingawa'),
            ('Jibia', 'Jibia'),
            ('Kafur', 'Kafur'),
            ('Kaita', 'Kaita'),
            ('Kankara', 'Kankara'),
            ('Kankia', 'Kankia'),
            ('Katsina', 'Katsina'),
            ('Kurfi', 'Kurfi'),
            ('Kusada', 'Kusada'),
            ('Mai''Adua', 'Mai''Adua'),
            ('Malumfashi', 'Malumfashi'),
            ('Mani', 'Mani'),
            ('Mashi', 'Mashi'),
            ('Matazu', 'Matazu'),
            ('Musawa', 'Musawa'),
            ('Rimi', 'Rimi'),
            ('Sabuwa', 'Sabuwa'),
            ('Safana', 'Safana'),
            ('Sandamu', 'Sandamu'),
            ('Zango', 'Zango'),
        )),
        ('Kebbi LGA', (
            ('Aleiro', 'Aleiro'),
            ('Arewa Dandi', 'Arewa Dandi'),
            ('Argungu', 'Argungu'),
            ('Augie', 'Augie'),
            ('Bagudo', 'Bagudo'),
            ('Birnin Kebbi', 'Birnin Kebbi'),
            ('Bunza', 'Bunza'),
            ('Dandi', 'Dandi'),
            ('Fakai', 'Fakai'),
            ('Gwandu', 'Gwandu'),
            ('Jega', 'Jega'),
            ('Kalgo', 'Kalgo'),
            ('Koko-Besse', 'Koko-Besse'),
            ('Maiyama', 'Maiyama'),
            ('Ngaski', 'Ngaski'),
            ('Sakaba', 'Sakaba'),
            ('Shanga', 'Shanga'),
            ('Suru', 'Suru'),
            ('Wasagu-Danko', 'Wasagu-Danko'),
            ('Yauri', 'Yauri'),
            ('Zuru', 'Zuru'),
        )),
        ('Kogi LGA', (
            ('Adavi', 'Adavi'),
            ('Ajaokuta', 'Ajaokuta'),
            ('Ankpa', 'Ankpa'),
            ('Bassa', 'Bassa'),
            ('Dekina', 'Dekina'),
            ('Ibaji', 'Ibaji'),
            ('Idah', 'Idah'),
            ('Igalamela Odolu', 'Igalamela Odolu'),
            ('Ijumu', 'Ijumu'),
            ('Kabba-Bunu', 'Kabba-Bunu'),
            ('Kogi', 'Kogi'),
            ('Lokoja', 'Lokoja'),
            ('Mopa Muro', 'Mopa Muro'),
            ('Ofu', 'Ofu'),
            ('Ogori-Magongo', 'Ogori-Magongo'),
            ('Okehi', 'Okehi'),
            ('Okene', 'Okene'),
            ('Olamaboro', 'Olamaboro'),
            ('Omala', 'Omala'),
            ('Yagba East', 'Yagba East'),
            ('Yagba West', 'Yagba West'),
        )),
        ('Kwara LGA', (
            ('Asa', 'Asa'),
            ('Baruten', 'Baruten'),
            ('Edu', 'Edu'),
            ('Ekiti-Kwara', 'Ekiti-Kwara'),
            ('Ifelodun', 'Ifelodun'),
            ('Ilorin East', 'Ilorin East'),
            ('Ilorin South', 'Ilorin South'),
            ('Ilorin West', 'Ilorin West'),
            ('Irepodun', 'Irepodun'),
            ('Isin', 'Isin'),
            ('Kaiama', 'Kaiama'),
            ('Moro', 'Moro'),
            ('Offa', 'Offa'),
            ('Oke Ero', 'Oke Ero'),
            ('Oyun', 'Oyun'),
            ('Pategi', 'Pategi'),
        )),
        ('Lagos LGA', (
            ('Agege', 'Agege'),
            ('Ajeromi-Ifelodun', 'Ajeromi-Ifelodun'),
            ('Alimosho', 'Alimosho'),
            ('Amuwo-Odofin', 'Amuwo-Odofin'),
            ('Apapa', 'Apapa'),
            ('Badagry', 'Badagry'),
            ('Epe', 'Epe'),
            ('Eti Osa', 'Eti Osa'),
            ('Ibeju-Lekki', 'Ibeju-Lekki'),
            ('Ifako-Ijaiye', 'Ifako-Ijaiye'),
            ('Ikeja', 'Ikeja'),
            ('Ikorodu', 'Ikorodu'),
            ('Kosofe', 'Kosofe'),
            ('Lagos Island', 'Lagos Island'),
            ('Lagos Mainland', 'Lagos Mainland'),
            ('Mushin', 'Mushin'),
            ('Ojo', 'Ojo'),
            ('Oshodi-Isolo', 'Oshodi-Isolo'),
            ('Shomolu', 'Shomolu'),
            ('Surulere-Lagos', 'Surulere-Lagos'),
        )),
        ('Nasarawa LGA', (
            ('Akwanga', 'Akwanga'),
            ('Awe', 'Awe'),
            ('Doma', 'Doma'),
            ('Karu', 'Karu'),
            ('Keana', 'Keana'),
            ('Keffi', 'Keffi'),
            ('Kokona', 'Kokona'),
            ('Lafia', 'Lafia'),
            ('Nasarawa', 'Nasarawa'),
            ('Nasarawa Egon', 'Nasarawa Egon'),
            ('Obi', 'Obi'),
            ('Toto', 'Toto'),
            ('Wamba', 'Wamba'),
        )),
        ('Niger LGA', (
            ('Agaie', 'Agaie'),
            ('Agwara', 'Agwara'),
            ('Bida', 'Bida'),
            ('Borgu', 'Borgu'),
            ('Bosso', 'Bosso'),
            ('Chanchaga', 'Chanchaga'),
            ('Edati', 'Edati'),
            ('Gbako', 'Gbako'),
            ('Gurara', 'Gurara'),
            ('Katcha', 'Katcha'),
            ('Kontagora', 'Kontagora'),
            ('Lapai', 'Lapai'),
            ('Lavun', 'Lavun'),
            ('Magama', 'Magama'),
            ('Mariga', 'Mariga'),
            ('Mashegu', 'Mashegu'),
            ('Mokwa', 'Mokwa'),
            ('Moya', 'Moya'),
            ('Paikoro', 'Paikoro'),
            ('Rafi', 'Rafi'),
            ('Rijau', 'Rijau'),
            ('Shiroro', 'Shiroro'),
            ('Suleja', 'Suleja'),
            ('Tafa', 'Tafa'),
            ('Wushishi', 'Wushishi'),
        )),
        ('Ogun LGA', (
            ('Abeokuta North', 'Abeokuta North'),
            ('Abeokuta South', 'Abeokuta South'),
            ('Ado-Odo-Ota', 'Ado-Odo-Ota'),
            ('Egbado North', 'Egbado North'),
            ('Egbado South', 'Egbado South'),
            ('Ewekoro', 'Ewekoro'),
            ('Ifo', 'Ifo'),
            ('Ijebu East', 'Ijebu East'),
            ('Ijebu North', 'Ijebu North'),
            ('Ijebu North East', 'Ijebu North East'),
            ('Ijebu Ode', 'Ijebu Ode'),
            ('Ikenne', 'Ikenne'),
            ('Imeko Afon', 'Imeko Afon'),
            ('Ipokia', 'Ipokia'),
            ('Obafemi Owode', 'Obafemi Owode'),
            ('Odeda', 'Odeda'),
            ('Odogbolu', 'Odogbolu'),
            ('Ogun Waterside', 'Ogun Waterside'),
            ('Remo North', 'Remo North'),
            ('Shagamu', 'Shagamu'),
        )),
        ('Ondo LGA', (
            ('Akoko North-East', 'Akoko North-East'),
            ('Akoko North-West', 'Akoko North-West'),
            ('Akoko South-West', 'Akoko South-West'),
            ('Akoko South-East', 'Akoko South-East'),
            ('Akure North', 'Akure North'),
            ('Akure South', 'Akure South'),
            ('Ese Odo', 'Ese Odo'),
            ('Idanre', 'Idanre'),
            ('Ifedore', 'Ifedore'),
            ('Ilaje', 'Ilaje'),
            ('Ile Oluji-Okeigbo', 'Ile Oluji-Okeigbo'),
            ('Irele', 'Irele'),
            ('Odigbo', 'Odigbo'),
            ('Okitipupa', 'Okitipupa'),
            ('Ondo East', 'Ondo East'),
            ('Ondo West', 'Ondo West'),
            ('Ose', 'Ose'),
            ('Owo', 'Owo'),
        )),
        ('Osun LGA', (
            ('Atakunmosa East', 'Atakunmosa East'),
            ('Atakunmosa West', 'Atakunmosa West'),
            ('Aiyedaade', 'Aiyedaade'),
            ('Aiyedire', 'Aiyedire'),
            ('Boluwaduro', 'Boluwaduro'),
            ('Boripe', 'Boripe'),
            ('Ede North', 'Ede North'),
            ('Ede South', 'Ede South'),
            ('Ife Central', 'Ife Central'),
            ('Ife East', 'Ife East'),
            ('Ife North', 'Ife North'),
            ('Ife South', 'Ife South'),
            ('Egbedore', 'Egbedore'),
            ('Ejigbo', 'Ejigbo'),
            ('Ifedayo', 'Ifedayo'),
            ('Ifelodun', 'Ifelodun'),
            ('Ila', 'Ila'),
            ('Ilesa East', 'Ilesa East'),
            ('Ilesa West', 'Ilesa West'),
            ('Irepodun', 'Irepodun'),
            ('Irewole', 'Irewole'),
            ('Isokan', 'Isokan'),
            ('Iwo', 'Iwo'),
            ('Obokun', 'Obokun'),
            ('Odo Otin', 'Odo Otin'),
            ('Ola Oluwa', 'Ola Oluwa'),
            ('Olorunda', 'Olorunda'),
            ('Oriade', 'Oriade'),
            ('Orolu', 'Orolu'),
            ('Osogbo', 'Osogbo'),
        )),
        ('Oyo LGA', (
            ('Afijio', 'Afijio'),
            ('Akinyele', 'Akinyele'),
            ('Atiba', 'Atiba'),
            ('Atisbo', 'Atisbo'),
            ('Egbeda', 'Egbeda'),
            ('Ibadan North', 'Ibadan North'),
            ('Ibadan North-East', 'Ibadan North-East'),
            ('Ibadan North-West', 'Ibadan North-West'),
            ('Ibadan South-East', 'Ibadan South-East'),
            ('Ibadan South-West', 'Ibadan South-West'),
            ('Ibarapa Central', 'Ibarapa Central'),
            ('Ibarapa East', 'Ibarapa East'),
            ('Ibarapa North', 'Ibarapa North'),
            ('Ido', 'Ido'),
            ('Irepo', 'Irepo'),
            ('Iseyin', 'Iseyin'),
            ('Itesiwaju', 'Itesiwaju'),
            ('Iwajowa', 'Iwajowa'),
            ('Kajola', 'Kajola'),
            ('Lagelu', 'Lagelu'),
            ('Ogbomosho North', 'Ogbomosho North'),
            ('Ogbomosho South', 'Ogbomosho South'),
            ('Ogo Oluwa', 'Ogo Oluwa'),
            ('Olorunsogo', 'Olorunsogo'),
            ('Oluyole', 'Oluyole'),
            ('Ona Ara', 'Ona Ara'),
            ('Orelope', 'Orelope'),
            ('Ori Ire', 'Ori Ire'),
            ('Oyo', 'Oyo'),
            ('Oyo East', 'Oyo East'),
            ('Saki East', 'Saki East'),
            ('Saki West', 'Saki West'),
            ('Surulere-Oyo', 'Surulere-Oyo'),
        )),
        ('Plateau LGA', (
            ('Bokkos', 'Bokkos'),
            ('Barkin Ladi', 'Barkin Ladi'),
            ('Bassa', 'Bassa'),
            ('Jos East', 'Jos East'),
            ('Jos North', 'Jos North'),
            ('Jos South', 'Jos South'),
            ('Kanam', 'Kanam'),
            ('Kanke', 'Kanke'),
            ('Langtang South', 'Langtang South'),
            ('Langtang North', 'Langtang North'),
            ('Mangu', 'Mangu'),
            ('Mikang', 'Mikang'),
            ('Pankshin', 'Pankshin'),
            ('Qua''an Pan', 'Qua''an Pan'),
            ('Riyom', 'Riyom'),
            ('Shendam', 'Shendam'),
            ('Wase', 'Wase'),
        )),
        ('Rivers LGA', (
            ('Abua-Odual', 'Abua-Odual'),
            ('Ahoada East', 'Ahoada East'),
            ('Ahoada West', 'Ahoada West'),
            ('Akuku-Toru', 'Akuku-Toru'),
            ('Andoni', 'Andoni'),
            ('Asari-Toru', 'Asari-Toru'),
            ('Bonny', 'Bonny'),
            ('Degema', 'Degema'),
            ('Eleme', 'Eleme'),
            ('Emuoha', 'Emuoha'),
            ('Etche', 'Etche'),
            ('Gokana', 'Gokana'),
            ('Ikwerre', 'Ikwerre'),
            ('Khana', 'Khana'),
            ('Obio-Akpor', 'Obio-Akpor'),
            ('Ogba-Egbema-Ndoni', 'Ogba-Egbema-Ndoni'),
            ('Ogu-Bolo', 'Ogu-Bolo'),
            ('Okrika', 'Okrika'),
            ('Omuma', 'Omuma'),
            ('Opobo-Nkoro', 'Opobo-Nkoro'),
            ('Oyigbo', 'Oyigbo'),
            ('Port Harcourt', 'Port Harcourt'),
            ('Tai', 'Tai'),
        )),
        ('Sokoto LGA', (
            ('Binji', 'Binji'),
            ('Bodinga', 'Bodinga'),
            ('Dange Shuni', 'Dange Shuni'),
            ('Gada', 'Gada'),
            ('Goronyo', 'Goronyo'),
            ('Gudu', 'Gudu'),
            ('Gwadabawa', 'Gwadabawa'),
            ('Illela', 'Illela'),
            ('Isa', 'Isa'),
            ('Kebbe', 'Kebbe'),
            ('Kware', 'Kware'),
            ('Rabah', 'Rabah'),
            ('Sabon Birni', 'Sabon Birni'),
            ('Shagari', 'Shagari'),
            ('Silame', 'Silame'),
            ('Sokoto North', 'Sokoto North'),
            ('Sokoto South', 'Sokoto South'),
            ('Tambuwal', 'Tambuwal'),
            ('Tangaza', 'Tangaza'),
            ('Tureta', 'Tureta'),
            ('Wamako', 'Wamako'),
            ('Wurno', 'Wurno'),
            ('Yabo', 'Yabo'),
        )),
        ('Taraba LGA', (
            ('Ardo Kola', 'Ardo Kola'),
            ('Bali', 'Bali'),
            ('Donga', 'Donga'),
            ('Gashaka', 'Gashaka'),
            ('Gassol', 'Gassol'),
            ('Ibi', 'Ibi'),
            ('Jalingo', 'Jalingo'),
            ('Karim Lamido', 'Karim Lamido'),
            ('Kumi', 'Kumi'),
            ('Lau', 'Lau'),
            ('Sardauna', 'Sardauna'),
            ('Takum', 'Takum'),
            ('Ussa', 'Ussa'),
            ('Wukari', 'Wukari'),
            ('Yorro', 'Yorro'),
            ('Zing', 'Zing'),
        )),
        ('Yobe LGA', (
            ('Bade', 'Bade'),
            ('Bursari', 'Bursari'),
            ('Damaturu', 'Damaturu'),
            ('Fika', 'Fika'),
            ('Fune', 'Fune'),
            ('Geidam', 'Geidam'),
            ('Gujba', 'Gujba'),
            ('Gulani', 'Gulani'),
            ('Jakusko', 'Jakusko'),
            ('Karasuwa', 'Karasuwa'),
            ('Machina', 'Machina'),
            ('Nangere', 'Nangere'),
            ('Nguru', 'Nguru'),
            ('Potiskum', 'Potiskum'),
            ('Tarmuwa', 'Tarmuwa'),
            ('Yunusari', 'Yunusari'),
            ('Yusufari', 'Yusufari'),
        )),
        ('Zamfara LGA', (
            ('Anka', 'Anka'),
            ('Bakura', 'Bakura'),
            ('Birnin Magaji-Kiyaw', 'Birnin Magaji-Kiyaw'),
            ('Bukkuyum', 'Bukkuyum'),
            ('Bungudu', 'Bungudu'),
            ('Gummi', 'Gummi'),
            ('Gusau', 'Gusau'),
            ('Kaura Namoda', 'Kaura Namoda'),
            ('Maradun', 'Maradun'),
            ('Maru', 'Maru'),
            ('Shinkafi', 'Shinkafi'),
            ('Talata Mafara', 'Talata Mafara'),
            ('Chafe', 'Chafe'),
            ('Zurmi', 'Zurmi'),
        )), 
        (None, 'Select a LGA')       
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
    state = models.CharField(max_length=50, choices=STATE_CHOICE)
    lga = models.CharField(_('LGA'), max_length=50, choices=LGA_CHOICE) #, blank=True, null=True, default='N/A')
    #city = models.CharField(max_length=50, null=True, blank=True)
    town = models.CharField(max_length=50)
    street = models.CharField(max_length=640)
    address = models.CharField(max_length=1000)
    
    approval_number = models.CharField(_('Govt Approval Number'), max_length=11, default='Awaiting')
    admin = models.CharField(_('Admission Officer'), max_length=128)
    founded = models.DateField(null=True, blank=True)

    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, default='mx') # max_choices is 1 - use default
    boarding = models.CharField(max_length=2, choices=BOARDING_CHOICE, default='bd') # max_choices is 1 - use default
    description = models.CharField(max_length=1000)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


    # School Choice Region
    creche = models.BooleanField(_('Creche'), default=False)
    nursery = models.BooleanField(_('Nursery'), default=False)
    primary = models.BooleanField(_('Primary'), default=False)
    secondary = models.BooleanField(_('Secondary'), default=False)
    aLevels = models.BooleanField(_('A-Levels'), default=False)

    # Approved Exams Choice Region
    ncee = models.BooleanField(_('National Common Entrance'), default=False)
    scee = models.BooleanField(_('State Common Entrance'), default=False)
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
    carol = models.BooleanField(_('Carol'), default=False)
    interhousesports = models.BooleanField(_('Inter House Sports'), default=False)
    culturalday = models.BooleanField(_('Cultural Day'), default=False)
    dance = models.BooleanField(_('Dance'), default=False)
    spellingbees = models.BooleanField(_('Spelling Bees'), default=False)
    debate = models.BooleanField(_('Debate'), default=False)
    quiz = models.BooleanField(_('Quiz'), default=False)
    swimming = models.BooleanField(_('Swimming'), default=False)
    karate = models.BooleanField(_('Karate'), default=False)
    costumeday = models.BooleanField(_('Costume Day'), default=False)

    # Clubs Choice Region
    gguide = models.BooleanField(_('Girl\'s Guide'), default=False)
    bscout = models.BooleanField(_('Boy\'s Scout'), default=False)
    frsc = models.BooleanField(_('FRSC'), default=False)
    music = models.BooleanField(_('Music'), default=False)
    drama = models.BooleanField(_('Drama'), default=False)
    #debate = models.BooleanField(default=False)
    press = models.BooleanField(_('Press'), default=False)
    jets = models.BooleanField(_('JETs'), default=False)
    karate = models.BooleanField(_('Karate'), default=False)
    rcross = models.BooleanField(_('Red Cross'), default=False)
    artscraft = models.BooleanField(_('Arts and Craft'), default=False)

    # Facility Choice Region
    sickbay = models.BooleanField(_('Sickbay'), default=False)
    multipurposehall = models.BooleanField(_('Multipurpose Hall'), default=False)
    sciencelab = models.BooleanField(_('Science Lab'), default=False)
    busservice = models.BooleanField(_('Bus Service'), default=False)
    library = models.BooleanField(_('Library'), default=False)
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

    verified = models.BooleanField(_('Verified'), default=False)

    def get_absolute_url(self):
        """Returns the url to access a particular school instance."""
        
        return reverse('school-detail', args=[str(self.slug)]) # school-detail is a view

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'


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

class SchoolGalleryImage(models.Model):
    '''Model for a School Gallery Images.'''
    img_1 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_2 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_3 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_4 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_5 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_6 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_7 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_8 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_9 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    img_10 = models.ImageField(upload_to='schools/<school_name>/gallery', blank=True)
    banner_img = models.ImageField(upload_to="schools/School.slug/gallery", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)


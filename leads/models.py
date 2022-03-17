from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


#01 - Agent (Lead Owner)
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Lead(models.Model):

    STATUS_ALT = (
    ('New_Lead', '01.New Lead'),
    ('Contacted', '02.Contacted'),
    ('Pre-Qualified', '03.Pre-Qualified'),
    ('Qualified', '04.Qualified'),
    ('Junk', '00.Junk'),
    ('Converted', '99.Converted')
    )

    SOURCE_ALT = (
    ('Youtube', 'Youtube'),
    ('Facebook', 'Facebook'),
    ('E-mail', 'E-mail'),
    ('Telephone', 'Telephone')
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    contact = PhoneNumberField(null=False, blank=False, unique=True)
    age = models.IntegerField(default=0)
    company = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    source =models.CharField(choices=SOURCE_ALT, max_length=50)
    status = models.CharField(choices=STATUS_ALT, max_length=50)
    lead_owner = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True)

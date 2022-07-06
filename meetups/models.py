from distutils.command.upload import upload
import email
from pydoc import describe
from unicodedata import name
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.name} - {self.address}'
class Joiners(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(max_length=200 )
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='imgs')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    joiners = models.ManyToManyField(Joiners , blank=True , null=True)

    def __str__(self):
        return f'{self.title} - {self.slug}'




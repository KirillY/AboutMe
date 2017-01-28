from django.db import models


# Create your models here.

class Organization(models.Model):
    name = models.CharField(verbose_name='Organization name', max_length=32)
    region = models.CharField(verbose_name='Organization location', max_length=32, blank=True)
    type_choices = (
        ('ED', 'Education'),
        ('BS', 'Business')
    )
    type = models.CharField(
        max_length = 2,
        choices = type_choices,
        default = 'BS', verbose_name='Organization type'
        )
    site = models.CharField(verbose_name='Organization website', max_length=32, blank=True)

class Work(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Organization name')
    period = models.PositiveIntegerField(verbose_name='Work length, months', default=1)
    position = models.CharField(verbose_name='Position', max_length=16)

class Person(models.Model):
    firstname = models.CharField(verbose_name='Fist name', max_length=16)
    lastname = models.CharField (verbose_name='Last name', max_length=16)
    born = models.DateField (verbose_name='Date of birth', blank=True)
    place = models.CharField(verbose_name='Place of birth', max_length=32)

class Education(models.Model):
    organization = models.ForeignKey(Organization, verbose_name='Organization name')
    year = models.DateField(verbose_name='Graduation year')

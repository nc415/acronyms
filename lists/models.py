from django.db import models
from django.conf.urls import patterns, include, url
from django.template.defaultfilters import slugify
import string
from datetime import datetime
# Create your models here.
class Acronyms(models.Model):
	name=models.CharField(max_length=300)
	name_only=models.CharField(max_length=300)

	def __str__(self):
		return self.name_only
	def __str__(self):
			return self.name

class Translation(models.Model):
	translation_item=models.CharField(max_length=500)
	

class Site(models.Model):
	site_name=models.CharField(max_length=200, unique=True)
	def __str__(self):
			return self.site_name
class University(models.Model):
	site = models.ForeignKey(Site, default=0)
	university_name=models.CharField(max_length=128, unique=True)
	university_acronym=models.CharField(max_length=128, unique=True)
	RAG_CHOICES = (
		('Y', 'Yes'),
		('N', 'No'),
		)
	rag=models.CharField(max_length=1, choices=RAG_CHOICES)


	
# Define as slug to use as the URL
	slug = models.SlugField(blank=True, unique=True)


# override default save to allow for the saving of the name with slugify filter
# This filter removes the spaces in multiple word sentences e.g. hello world becomes hello-world
#.join(random.sample(string.ascii_lowercase, 1))
	'''def validate_unique(self, exclude=None):
		qs = Person.objects.filter(name=self.name)
		raise ValidationError('Name must be unique per site')
		'''

	def save(self, *args, **kwargs):
		
		university_name=str(self.university_name)
		self.slug=slugify(university_name)
		
		super(University, self).save(*args, **kwargs)

# Fix issue where the plural of category is categories NOT categorys
	def __str__(self):
			return self.university_name


class Society(models.Model):
	site=models.ForeignKey(Site, default=0)
	university=models.ForeignKey(University, default=0)
	society_name=models.CharField(max_length=256, unique=True)
	society_acronym=models.CharField(max_length=100, unique=False, blank=True)
	society_email=models.EmailField(max_length=254, blank=True)
	STATUS_CHOICES = (
		('P', 'PASSED'),
		('U', 'UNKNOWN'),
		('F', 'FAILED'),
		)
	society_email_status=models.CharField(max_length=1, choices=STATUS_CHOICES)
	CONTACT_STATUS_CHOICES =(
		('1', 'Whitelist'),
		('2', 'Blacklist'),
		('3', 'Neutral'),
		)
	society_contact_status=models.CharField(max_length=1, choices=CONTACT_STATUS_CHOICES)
	society_slug = models.SlugField(blank=True, unique=True)
	notes=models.TextField(blank=True, default="")

	def save (self, *args, **kwargs):
		society_name=str(self.society_name)
		self.society_slug=slugify(society_name)
		super(Society, self).save(*args, **kwargs)

	def __str__(self):
		return self.society_name##

class EmailHistory(models.Model):
	last_emailed=models.DateTimeField(default=datetime.now())
	society=models.ForeignKey(Society, default=0)
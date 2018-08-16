from django.db import models
from django.conf import settings
from .utils import code_generator,create_shortcode
#from .forms import validate_url
# Create your models here.

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)


class RytzURL(models.Model):
	url 		= models.CharField(max_length=220)
	shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True,null=True)
	count 		= models.PositiveIntegerField(default=0)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp   = models.DateTimeField(auto_now_add=True)
	active 		= models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(RytzURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

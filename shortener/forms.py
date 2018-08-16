from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from .models import RytzURL


#this function same as clean method written in below class...this method has advantage...we can also validate
#fields in admin section also..and for this you have to include validator argument in model field..see in model.py
#...whereas clean method only validate forms..
def validate_url(value):
	url_validator = URLValidator()
	try:
		url_validator(value)
	except:
		raise ValidationError("Please provide valid URL")

class SubmitUrlForm(forms.ModelForm):
	url       = forms.CharField(validators=[validate_url])

	class Meta:
		model = RytzURL
		fields = ['url','shortcode',]




       


	# class Meta:
	# 	model = RytzURL
	# 	fields = ['url',]


#,widget=forms.Textarea(attrs={'placeholder':'efe','cols': 1, 'rows': 2})
#### this is also correct

# class SubmitUrlForm(forms.ModelForm):
# 	url = forms.CharField(label="Submit URL")

# 	class Meta:
# 		model = RytzURL
# 		fields = ['url',]

# 	def clean(self):
# 		cleaned_data = super(SubmitUrlForm,self).clean()
# 		url = cleaned_data.get('url')
# 		url_validator = URLValidator()
# 		try:
# 			url_validator(url)
# 		except:
# 			raise forms.ValidationError("Invalid URL for this field")
# 		return url


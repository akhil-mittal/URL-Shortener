from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from .models import RytzURL
from .forms import SubmitUrlForm


def Home(request):
	form = SubmitUrlForm(request.POST or None)
	context = {
	   "form" : form,
	}
	template = 'shortener/home.html'
	if form.is_valid():
		new_url = form.cleaned_data.get("url")
		new_shortcode = form.cleaned_data.get("shortcode")
		obj = RytzURL.objects.filter(url=new_url)
		shortcode_already_exists = None
		created = None
		if not obj and not new_shortcode:
			created = RytzURL.objects.create(url=new_url)
			return render(request,'shortener/success.html',{"created":created,"form":form})
		elif not obj and new_shortcode:
			print("erer")
			shortcode_get  = RytzURL.objects.filter(shortcode=new_shortcode)
			if not shortcode_get:
				form.url = new_url
				form.shortcode = new_shortcode
				form.save()
				obj = RytzURL.objects.get(url=new_url)
				return render(request,'shortener/short-available.html',{"object":obj,"form":form})
			else:
				print("erer")
				return render(request,'shortener/shortcode-exists.html',{"form":form})
		elif obj and not new_shortcode:
			obj = RytzURL.objects.get(url=new_url)
			return render(request,'shortener/success.html',{"object":obj,"form":form})

		elif obj and new_shortcode:
			obj = RytzURL.objects.get(url=new_url)
			return render(request,'shortener/url-exists.html',{"object":obj,"form":form})
	return render(request,template,context)


class RytzCBView(View):
	def get(self, request,shortcode=None, *args, **kwargs):
		obj = get_object_or_404(RytzURL,shortcode=shortcode)
		obj.count += 1
		obj.save()
		return HttpResponseRedirect(obj.url)

def is_available(request):
	context = {}
	is_available = False
	if request.method == 'POST' :
		shortcode = request.POST['shortcode']
		try:
			obj = get_object_or_404(RytzURL,shortcode=shortcode)
		except Http404:
			is_available = True

	context['is_available'] = is_available

	return JsonResponse(context)




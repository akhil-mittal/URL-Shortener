"""rytz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from shortener.views import Home, RytzCBView, is_available

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',Home),
    url(r'^(?P<shortcode>[\w-]+)/$',RytzCBView.as_view()),
    url(r'^shortcode/is_available/$', is_available,name='is_available'),
]
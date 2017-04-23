from django.conf.urls import  include, url

from . import views

app_name = 'url_shortener'

urlpatterns = [
    # home
    url(r'^$', views.index, name='index'),

    # redirecting short URL to original (long) URL
    url(r'^(?P<url_id>\w{6})$', views.redirect, name='redirect'),
]

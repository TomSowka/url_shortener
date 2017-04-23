# url_shortening URL Configuration

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    #admin
    url(r'^admin/', admin.site.urls),

    # if anything other than admin/ use patterns in url_shortening/urls.py
    url(r'', include('url_shortener.urls', namespace='url_shortening')),
]

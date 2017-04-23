from django.shortcuts import render, get_object_or_404
import json, random, string
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F

from .models import URL
from .forms import URLForm

# startpage view
def index(request):
    form = URLForm();
    short_url = None;
    if request.method == 'POST':
        form = URLForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['your_url']
            hostname = format(request.META['HTTP_HOST'])
            short_url = '' + hostname + "/" + shorten_url(url)
    return render(request, 'url_shortener/index.html', {'form': form, 'short_url':short_url})

# redirect from short to original url
def redirect(request, url_id):
    url = get_object_or_404(URL, pk=url_id) # get URL object or return 404
    url.visited = F('visited') + 1
    url.save()
    return HttpResponseRedirect(url.long_url)

# shorten given url
def shorten_url(url):

    if (url != ''):

       url_id = generate_short_id()

       #update object, --> DB
       url_object  = URL(long_url = url, url_id = url_id)
       url_object.save()

       return url_id

    else:
        return

# generate url_id
def generate_short_id():
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    #  if url_id already exists, retry with a new one
    while True:
        url_id = ''.join(random.choice(char) for x in range(6))
        try:
            occupied = Urls.objects.get(pk=short_id)
        except:
            return url_id

from django.db import models

from django.db import models

# Create your models here.
class URL( models.Model ):
    url_id = models.SlugField(max_length=6,primary_key=True)
    long_url = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    visited = models.IntegerField(default=0)

def __str__(self):
    return self.long_url

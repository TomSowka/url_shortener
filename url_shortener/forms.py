from django import forms

class URLForm (forms.Form):
    your_url = forms.CharField(label='URL:', max_length=200)

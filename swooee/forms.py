from django.forms import ModelForm
from .models import *
from django import forms

class Static_pageForm(forms.ModelForm):  
    class Meta:
        model = Static_page
        fields  = ('title','contain','Image')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control p-input','placeholder':'Enter Title For Static Page'}),
            'contain' : forms.TextInput(attrs={'class':'form-control p-input'}),
            'Image' : forms.FileInput(attrs={'class':'form-control file-upload-info'}),
        }
        
class BannerForm(forms.ModelForm):  
    class Meta:
        model = Banner
        fields  = ('short_title','contain','file')
        widgets = {
            'short_title' : forms.TextInput(attrs={'class':'form-control p-input','placeholder':'Enter Title For Banner '}),
            'contain' : forms.TextInput(attrs={'class':'form-control p-input'}),
            'file' : forms.FileInput(attrs={'class':'form-control file-upload-info'}),
        }

from django import forms
from django.forms import ModelForm
from .models import Upload

class SaveUploaded(ModelForm):
    class Meta:
        model = Upload
        fields = ['image','watermark','flag','alpha']
from django import forms
from .models import BMPImage

class BMPImageForm(forms.ModelForm):
    class Meta:
        model = BMPImage
        fields = ['name', 'image']

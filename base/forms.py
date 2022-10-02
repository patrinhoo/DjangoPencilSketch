from django import forms
from .models import OriginalImage, Images


class ImageForm(forms.ModelForm):
    class Meta:
        model = OriginalImage
        fields = '__all__'

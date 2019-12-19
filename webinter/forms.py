from django import forms
from .models import UploadFile

class UploadFileForm(forms.Form):
    class Meta:
        madel = UploadFile
        fields = ['owner']
        labels = {'owner': ''}
    # title = forms.CharField(max_length=50)
    # file = forms.FileField()
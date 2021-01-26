from django import forms


class FileUpload(forms.Form):
    title = forms.CharField(max_length=64)
    file = forms.FileField()

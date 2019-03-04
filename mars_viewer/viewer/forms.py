from django import forms

class FileUploadForm(forms.Form):
    title = forms.CharField(max_length=100, label='File name', initial='dates.txt')
    file = forms.FileField()
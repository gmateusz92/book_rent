from django import forms 
#from .choices import FORMAT_CHOICES


class SearchBookForm(forms.Form):
    search = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'search by book id ...'}))
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('full_name', 'email', 'phone', 'upload_cv', 'coverletter', )

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'upload_cv': forms.FileInput(attrs={'class': 'form-control'}),
            'coverletter': forms.Textarea(attrs={'class':'form-control'}),
            }
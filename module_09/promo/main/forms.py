from django import forms
from .models import *
from users.models import *


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'company_description', 'users']
        widgets = {
            'company_description': forms.Textarea(attrs={'cols': 60, 'rows': 3})
        }

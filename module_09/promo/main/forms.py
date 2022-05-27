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


class AddHouseForm(forms.ModelForm):
    class Meta:
        model = House
        company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, to_field_name='company')
        fields = ['city', 'street', 'house_number', 'numbers_entrance', 'numbers_apartment', 'company']


class AddUserToCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'users']

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from users.models import CustomUser
from .models import House, Company
from .forms import AddCompanyForm, AddHouseForm, AddUserToCompanyForm

# Create your views here.


def main(response):
    data = Company.objects.all()
    return render(response, "main/main.html", {"companies": data})


def company(response, company_id):
    data = House.objects.filter(company_id=company_id)
    name_company = Company.objects.get(pk=company_id)
    users = CustomUser.objects.filter(company=company_id)
    return render(response, "main/company.html", {"data": data, "company": name_company, "users": users})


def my_company(response, user_id):
    name_company = Company.objects.filter(users=user_id)
    return render(response, "main/mycompanies.html", {"companies": name_company})


def info(response):
    return render(response, "main/info.html")


def company_create(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main')
    else:
        form = AddCompanyForm()
    return render(request, "main/addcompany.html", {'form': form})


def add_house(request, company_id):
    name_company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Company', company_id=company_id)
    else:
        form = AddHouseForm(initial={'company': name_company})
    return render(request, "main/addhouse.html", {'form': form, 'company': name_company})


def add_user(request, company_id):
    name_company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        form = AddUserToCompanyForm(request.POST, instance=name_company)
        if form.is_valid():
            form.save()
            return redirect('Company', company_id=company_id)
    else:
        form = AddUserToCompanyForm(initial={'company_name': name_company}, instance=name_company)
    return render(request, "main/adduser.html", {'form': form, 'company': name_company})

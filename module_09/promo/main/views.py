from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import House, Company
from .forms import AddCompanyForm

# Create your views here.


def main(response):
    data = Company.objects.all()
    return render(response, "main/main.html", {"companies": data})


def company(response, company_id):
    data = House.objects.filter(company_id=company_id)
    name_company = Company.objects.get(pk=company_id)
    return render(response, "main/company.html", {"data": data, "company": name_company})


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

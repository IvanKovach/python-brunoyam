from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    data = {'data': [1, 2, 3], 'title': 'Index'}
    return render(response, "main/index.html", data)


def info(response):
    return render(response, "main/info.html")

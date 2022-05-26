from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='Main'),
    path('main', views.main, name='Main'),
    path('info', views.info, name='Info'),
    path('company/<int:company_id>', views.company, name='Company'),
    path('company/create', views.company_create, name='CompanyCreate'),
    path('mycompanies/<int:user_id>', views.my_company, name='MyCompanies')
]

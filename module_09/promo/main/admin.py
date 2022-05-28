from django.contrib import admin
from .models import Company, House, Apartment
# Register your models here.

admin.site.register(Company)
admin.site.register(House)
admin.site.register(Apartment)

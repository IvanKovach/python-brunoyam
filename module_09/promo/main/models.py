from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.models import CustomUser


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_description = models.CharField(max_length=255)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "PromoCompany"
        verbose_name_plural = "PromoCompanies"


class House(models.Model):
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house_number = models.CharField(max_length=5)
    numbers_entrance = models.IntegerField()
    numbers_apartment = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return self.city + ', ' + self.street + ' ' + self.house_number

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"


class Apartment(models.Model):
    apartment_number = models.IntegerField()
    entrance_number = models.IntegerField()
    is_open = models.BooleanField(default=False)
    owners_name = models.CharField(max_length=200)
    owners_phone = PhoneNumberField(blank=True)
    comment = models.CharField(max_length=200)
    NEUTRAL = 'NT'
    POSITIVE = 'PS'
    NEGATIVE = 'NG'
    REACTION_TYPE = [
        (NEUTRAL, 'neutral'),
        (POSITIVE, 'positive'),
        (NEGATIVE, 'negative')
    ]
    reaction = models.CharField(max_length=2, choices=REACTION_TYPE, blank=False)
    house = models.ForeignKey(House, on_delete=models.PROTECT)

    def __str__(self):
        return self.apartment_number

    class Meta:
        verbose_name = "Apartment"
        verbose_name_plural = "Apartments"

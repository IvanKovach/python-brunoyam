from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    name = models.CharField('Имя', max_length=20, default='')
    surname = models.CharField('Фамилия', max_length=30, default='')
    phone_number = models.CharField('Номер телефона', max_length=13, default='')
    email = models.EmailField('Электронная почта', max_length=255, default='')
    birth_date = models.DateField('Дата рождения', blank=True, default='1900-01-01', null=True)

#    def __str__(self):
#        return self.surname + ' ' + self.name

#    class Meta:
#        verbose_name = "User"
#        verbose_name_plural = "Users"

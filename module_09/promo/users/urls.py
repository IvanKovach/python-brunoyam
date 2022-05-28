from django.urls import path, include
from . import views

urlpatterns = [
    path('lk', views.sign_in, name='users'),
    path('signup/', views.sign_up, name='sign_up'),
    path('change_profile/', views.change_profile, name='change_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change_data1/', views.change_data1, name='change_data1')
]

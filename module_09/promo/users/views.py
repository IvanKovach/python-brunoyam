from django.shortcuts import render
from .models import CustomUser
from .forms import RegisterForm, ChangeProfile, ChangeData1
from django.contrib.auth import authenticate, login, logout


def start(response):
    return render(response, "users/start.html")


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data_user = form.cleaned_data
            data = {'form': form}
            if CustomUser.objects.filter(username=data_user['username']).exists():
                return render(request, 'users/form_registration_alert.html', data)
            if data_user['password_1'] == data_user['password']:
                del data_user['password_1']
                user = CustomUser.objects.create_user(**data_user)
                user.save()
                return render(request, 'users/form_complete.html')
            else:
                return render(request, 'users/form_registration_alert_password.html', data)
        else:
            data = {'form': form}
            return render(request, 'users/form_registration_alert.html', data)
    form = RegisterForm()
    data = {'form': form}
    return render(request, 'users/form_registration.html', data)


def sign_in(request):
    return render(request, 'base2.html')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'users/login_success.html')
    else:
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return render(request, 'users/login.html')


def change_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    form = ChangeProfile()
    if request.method == "POST":
        form = ChangeProfile(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            if data_form['name']:
                user.name = data_form['name']
            if data_form['surname']:
                user.surname = data_form['surname']
            if data_form['phone_number']:
                user.phone_number = data_form['phone_number']
            if data_form['email']:
                user.email = data_form['email']

            user.save()
            return render(request, 'users/change_profile_complete.html')
    context = {'form': form}
    return render(request, 'users/change_profile.html', context=context)


def change_data1(request):
    user = CustomUser.objects.get(id=request.user.id)
    form = ChangeData1()
    if request.method == "POST":
        form = ChangeData1(request.POST)
        if form.is_valid():
            data_form = form.cleaned_data
            if data_form['username']:
                user.username = data_form['username']
            if data_form['password_1'] == data_form['password']:
                if data_form['password']:
                    user.set_password(data_form['password'])
            else:
                context = {'form': form}
                return render(request, 'users/change_data1_alert.html', context=context)
            user.save()
            return render(request, 'users/change_profile_complete.html')
    context = {'form': form}
    return render(request, 'users/change_data1.html', context=context)

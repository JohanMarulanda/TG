from django.shortcuts import render
from users.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'users/index.html')


@login_required
def special(request):
    return HttpResponse("Entraste al sistema !")


@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)

        return render(request,'users/user_login')


@login_required
def principalUser(request):
    return render(request, 'users/principalUser.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('Encontrado')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'users/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'users/principalUser.html')
            else:
                return HttpResponse("Tu cuenta esta inactiva.")
        else:
            print('Alguien ha intentado logearse y fallo')
            print("usaron el username: {} y la contraseña: {}".format(username, password))
            return HttpResponse("Datos erroneos para logearse")
    else:
        return render(request, 'users/login.html', {})

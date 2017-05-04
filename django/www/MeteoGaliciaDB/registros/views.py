from django.shortcuts import render
from . import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.



@login_required
def special(request):
    return HttpResponse("Estás logueado!")


@login_required
def user_logout(request):
    logout(request)
    logged = False
    return render(request, 'registros/login.html',{'logged':logged})



def registro(request):
    registered = False
    if request.method == 'POST':
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfo(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfo()
    return render(request,'registros/registration.html', {'registered': registered, 'user_form': user_form,'profile_form':profile_form})


def user_login(request):
    logged = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                logged = True
                return render(request, 'registros/login.html', {'logged': logged})
            else:
                return HttpResponse("Cuenta inactiva")
        else:
            print("Alguien intento loguearse y falló")
            return HttpResponse("Datos de acceso inválidos")
    else:
        return render(request, 'registros/login.html',{'logged':logged})
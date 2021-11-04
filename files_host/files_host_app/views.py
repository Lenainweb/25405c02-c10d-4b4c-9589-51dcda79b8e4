from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, request
from django.views.generic import TemplateView

from .models import File
from .forms import FileForm

def logout_user(request):
    """
    Remove the authenticated user's ID from the request and flush their session
    data.
    """
    logout(request)
    return redirect('login')

def login_user(request):
    """
    Persist a user id and a backend in the request. This way a user doesn't
    have to reauthenticate on every request. 
    """
    user_au = authenticate(username=request.POST['username'], password=request.POST['password'])
    login(request, user_au)

class HomePageView(TemplateView):
    
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            files = File.objects.all().order_by('count_download')            
            return render(request, 'files_host/index.html', context={'files': files})
        else:
            return redirect('login')

class AuthenticatedView(TemplateView):   
    
    def get(self, request, **kwargs): 
        login_form = AuthenticationForm()      
        return render(request, 'file_host_template/login.html', context={'login_form': login_form})
   
    def post(self, request, **kwargs):
        login_form = AuthenticationForm(request.POST)
        try:
            login_user(request)
        except:
            return redirect('login')
        return redirect('home')


class RegisterView(TemplateView):    

    def get(self, request, **kwargs):
        register_form = UserCreationForm()     
        return render(request, 'file_host_template/register.html', context={'register_form': register_form})
    
    def post(self, request, **kwargs):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save()
            new_user.save()
            user_au = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, user_au)               
            return redirect('home')
        return render(request, 'file_host_template/register.html', context={'register_form': register_form})   
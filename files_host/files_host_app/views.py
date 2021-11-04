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
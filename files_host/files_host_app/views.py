import uuid
from django.contrib.auth import models

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, request, FileResponse, response
from django.views.generic import TemplateView, DetailView

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


class AuthenticatedView(TemplateView):
    """ 
    user authentication page 
    """   
    
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
    """ 
    user registration page 
    """   

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


class HomePageView(TemplateView):
    """ 
    main page with a list of all public files 
    """
    
    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            files = File.objects.filter(permission_for_file="PUBLIC").order_by('-count_download')            
            return render(request, 'file_host_template/index.html', context={'files': files})
        else:
            if User.objects.filter(username="admin"):
                return redirect('login')
            else:
                user = User.objects.create_user('admin', 'admin@admin.com', 'admin')
            return redirect('login')

    

class AddFileView(TemplateView):
    """ 
    page with a file adding form 
    """

    def get(self, request, **kwargs):
        file_form = FileForm()     
        return render(request, 'file_host_template/add_file.html', context={'file_form': file_form})
    
    def post(self, request, **kwargs):
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            new_file = file_form.save(commit=False)
            file_data = file_form.cleaned_data.get("file")               
            new_file.original_filename = file_data.name
            new_file.guid_name = str(uuid.uuid4())
            new_file.owner = request.user
            new_file.save()                         
            return redirect('home')
        return render(request, 'file_host_template/add_file.html', context={'file_form': file_form})

class FileDetail(DetailView):
    """ 
    file details and download link 
    """

    model = File
    slug_field = "id"
    context_object_name = 'file_detail'
    template_name = "file_host_template/file_detail.html"

    # def get(self, request, **kwargs):
    #     if "file_download" in request.GET:
    #         file = File.objects.first(id="id")
    #         response = FileResponse(open(file, 'rb'))
    #         return HttpResponse(response)
    #     else:
    #         redirect('home')

class MyFilesView(TemplateView):
    """ 
    displays a list of files uploaded by the user 
    """

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            my_files = File.objects.filter(owner=request.user).order_by('count_download')            
            return render(request, 'file_host_template/my_files.html', context={'my_files': my_files})
        else:
            return redirect('login')

    

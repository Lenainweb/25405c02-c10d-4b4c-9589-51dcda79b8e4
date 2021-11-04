from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView, name='logout'),
    # path('register', auth_views.RegisterView.as_view(), name='register' )
]
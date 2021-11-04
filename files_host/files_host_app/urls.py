from django.urls import path
# from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('login', AuthenticatedView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register' ),
    path('logout', logout_user, name='logout'),
]
from django.urls import path
# from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('login', AuthenticatedView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register' ),
    path('logout', logout_user, name='logout'),
    path('add_file', AddFileView.as_view(), name='add_file'),
    # path('<slug:slug>/', FileDetail.as_view(), name='file_detail'),
    path('my_files', MyFilesView.as_view(), name = 'my_files'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
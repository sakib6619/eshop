from django.urls import path
from .views import *
urlpatterns = [
    path('login/',user_login, name='login'),
    path('signup/',signup, name='signup'),
    path('profile/',user_profile, name='profile'),
    path('logout/',user_logout, name='logout'),
    path('change_password/',change_password, name='change_pass')
]
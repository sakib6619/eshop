from django.urls import path
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('FAQ/',faq, name='faq'),
    path('blog/',blog, name='blog'),
    path('blog_details/',blog_details, name='blog_details'),
    path('404Error/', error4040, name='error404'),
]
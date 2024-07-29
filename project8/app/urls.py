from django.urls import path
from . views import *
urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('register_django_forms', register_django_forms, name='register_django_forms')

]

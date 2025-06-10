from django.urls import path
from .views import *

app_name = 'HomePage'

urlpatterns = [
    path('', homepage, name='homepage'),
]
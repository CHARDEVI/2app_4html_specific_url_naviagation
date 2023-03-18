from django.urls import path
from cricket.views import *
app_name='cricket'

urlpatterns=[
    path('sushanth/',sushanth,name='sushanth'),
    path('mahi/',mahi,name='mahi'),
]
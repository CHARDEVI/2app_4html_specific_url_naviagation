from django.urls import path
from sports.views import *
app_name='sports'

urlpatterns=[
    path('messi/',messi,name='messi'),
    path('ronaldo/',ronaldo,name='ronaldo'),
]
from django.urls import path
from rest_framework import urlpatterns
from .views import ReturnProfile

urlpatterns =[
    path('me/', ReturnProfile.as_view())
]


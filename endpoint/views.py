import datetime
from django.shortcuts import render
from .api import get_cat_fact
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ReturnProfile(APIView):
    def get(self, request, format = None):
        response = {
            "status": "success",
            "user":{
                "email": "ijjayeola@gmail.com",
                "name": "Jayeola, Ifeoluwa Joseph",
                "stack": "Python/Django"
            },
            "timestamp": datetime.datetime.now(),
            "fact": get_cat_fact()
        }
        return Response(response)

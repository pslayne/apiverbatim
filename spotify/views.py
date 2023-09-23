from django.shortcuts import render
from django.http import HttpResponse
from . import controller

# Create your views here.
def index(request):
    access_token = controller.getAccessToken()
    return HttpResponse(access_token)
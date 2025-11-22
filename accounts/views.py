from django.shortcuts import render
from django.http import HttpResponse

# account views

def login_view(request):
    return HttpResponse("Login page")

def signup_view(request):
    return HttpResponse("signup page")

def perks_view(request):
    return HttpResponse("perks page")




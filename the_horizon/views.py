from django.shortcuts import render
from django.http import HttpResponse

def horizon_overview(request):
    return HttpResponse("The Horizon - upcoming projects")

def horizon_update(request, update_id):
    return HttpResponse(f"Horizon updates for specific ID: {update_id}")

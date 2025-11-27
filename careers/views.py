from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jobs_list(request):
    return render(request, "careers.html")

def job_detail(request, job_id):
    return HttpResponse(f"Job detail page ID: {job_id}")

def job_apply(request, job_id):
    return HttpResponse(f"Apply page for a specific job ID: {job_id}")

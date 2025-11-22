from django.urls import path
from . import views

urlpatterns = [
    path('',views.jobs_list, name='jobs_list'),
    path('<int:job_id>/',views.job_detail, name='job_detail'),
    path('<int:job_id>/apply/',views.job_apply, name='job_apply'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.horizon_overview, name='horizon_overview'),
    path('<int:update_id>/', views.horizon_update, name='horizon_update'),
]
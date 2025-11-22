from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('perks/', views.perks_view, name='perks'),
]

# 1.match for account/(path) in url 2. call the view request, 3. let templates refer to the pattern url {% url 'name' %}

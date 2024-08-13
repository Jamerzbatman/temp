from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Replace 'scripts_view' with your actual view function name
]
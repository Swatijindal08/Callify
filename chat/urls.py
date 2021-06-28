from django.urls import path
from .views import main_view,home

urlpatterns = [
    path('', main_view, name='main_view'),
    path('home',home, name='home'),
    
]
from django.urls import path
from .views import main_view,home

urlpatterns = [
    path('',home, name='home'),
    path('call', main_view, name='main_view'),
    
    
]
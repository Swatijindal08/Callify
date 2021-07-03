from django.urls import path
from .views import main_view,home,msg_view

urlpatterns = [
    path('',home, name='home'),
    path('call', main_view, name='main_view'),
    path('msg', msg_view, name='msg_view'),
    
]
from django.urls import path

from core.app import views

urlpatterns = [
    path('', views.home, name='home'),
]
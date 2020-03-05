from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agency-home'),
    path('about/', views.about, name='agency-about'),
    path('property/<int:pk>/', views.pproperty, name='agency-property'),
]
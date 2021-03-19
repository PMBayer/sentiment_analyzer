from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='analyzer_home'),
    path('about/', views.about, name='analyzer_about'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('<str:category>/', views.dashboard, name='dashboard'),
]
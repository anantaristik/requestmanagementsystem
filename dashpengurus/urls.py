from . import views
from django.urls import path

urlpatterns = [
    path('<str:category>/', views.dashboard_pengurus, name='dashboard_pengurus'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('dashboard_pengurus/<str:category>/<str:sort>', views.dashboard_pengurus, name='dashboard_pengurus'),
]
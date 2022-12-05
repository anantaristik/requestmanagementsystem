from django.urls import path
from .views import index, keuangan

app_name = 'home'

urlpatterns = [
    path('', index, name='home'),
    path('keuangan', keuangan, name='keuangan'),
]
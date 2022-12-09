from django.urls import path
from .views import index, keuangan, surat, publikasi

app_name = 'home'

urlpatterns = [
    path('', index, name='home'),
    path('keuangan', keuangan, name='keuangan'),
    path('surat', surat, name='surat'),
    path('publikasi', publikasi, name='publikasi'),
]
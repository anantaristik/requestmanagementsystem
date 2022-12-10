from . import views
from django.urls import path

app_name = 'publikasi'

urlpatterns = [
    path('form', views.formPublikasi, name='formpublikasi'),
    path('postformpublikasi', views.postFormPublikasi, name='postformpublikasi'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('delete', views.delete, name='delete')
]
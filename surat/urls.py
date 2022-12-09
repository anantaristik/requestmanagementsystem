from . import views
from django.urls import path

app_name = 'surat'

urlpatterns = [
    path('form', views.formSurat, name='formsurat'),
    path('postformsurat', views.postFormSurat, name='postformsurat'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('delete', views.delete, name='delete')

]
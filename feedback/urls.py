from . import views
from django.urls import path

app_name = 'feedback'

urlpatterns = [
    path('form/<str:id>/<str:jenis>', views.formFeedback, name='formfeedback'),
    path('postformfeedback', views.postFormFeedback, name='postformfeedback'),
    path('detail/<str:id>', views.detail, name='detail'),
    path('delete', views.delete, name='delete')

]
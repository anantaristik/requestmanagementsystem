from django.urls import path
from .views import *

app_name = 'reimbursement'

urlpatterns = [
    path('form', form_reimbursement, name='form_reimbursement'),
    path('postForm', post_form_reimbursement, name='post_form_reimbursement'),
    path('detail/<str:id>', detail, name='detail')
]
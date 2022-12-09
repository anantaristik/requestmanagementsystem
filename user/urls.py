from .views import *
from django.urls import path

urlpatterns = [
    path('login', login, name='login'),
    path('postlogin', postLogin, name='postlogin'),
    path('signup', signUp, name='signup'),
    path('postsignup', postSignUp, name='postsignup'),
    path('dashboard', dashboard, name='dashboard')
]
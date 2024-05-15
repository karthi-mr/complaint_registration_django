from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login-user/', views.login_user, name='user-login'),
    path('register-user/', views.register_user, name='user-register'),
    path('logout-user/', views.logout_user, name='user-logout'),
]

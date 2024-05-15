from django.urls import path

from complaints import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='com-dashboard'),
    path('complaints/', views.complaints_list, name='complaint-list')
]

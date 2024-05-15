from django.urls import path

from complaints import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='com-dashboard'),
    path('', views.complaints_list, name='complaint-list'),
    path('new/', views.create_complaint, name='create-complaint'),
    path('edit/<int:pk>', views.edit_complaint, name='edit-complaint'),
]

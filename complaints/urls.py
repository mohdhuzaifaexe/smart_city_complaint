from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('submit-complaint/',views.submit_complaint,name='submit_complaint'),

    path('my-complaints/',views.my_complaints,name='my_complaints'),

    path('complaint/<int:complaint_id>/',views.complaint_detail,name='complaint_detail'),

    path('admin-dashboard/',views.admin_dashboard,name='admin_dashboard'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('seller/register/', views.seller_register, name='seller_register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('seller/dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

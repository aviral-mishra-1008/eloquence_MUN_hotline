from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('send-to-eb/', views.send_message_to_eb, name='send_to_eb'),
    path('send-to-nation/', views.send_message_to_nation, name='send_to_nation'),
    path('messages/', views.messages, name='messages'),
    path('notifications/', views.notifications, name='notifications'),
    path('generate-credentials/', views.generate_credentials, name='generate_credentials'),
    path('manage-users/', views.user_management, name='user_management'),
]
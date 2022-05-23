from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home_login'),
    path('register/', views.registration_view, name='register'),
    path('profile/<str:pk>', views.profile, name='profile')
]
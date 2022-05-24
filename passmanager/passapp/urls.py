from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home_login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='register'),
    path('myprofile/<str:pk>', views.profile_view, name='profile'),
    path('add/<str:pk>', views.add_creds_view, name='add-creds')
]
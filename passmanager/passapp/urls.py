from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home_login')
]
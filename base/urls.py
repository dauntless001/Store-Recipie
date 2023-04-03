from django.urls import path
from base import views


app_name = 'base'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
from django.urls import path
from main import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_with_metamask, name='login_with_metamask'),
    path('profile/', views.profile, name='profile'),
]

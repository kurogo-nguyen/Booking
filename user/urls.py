from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# from django.views.generic import ListView, DetailView

urlpatterns = [
    path('register/', views.register, name="register"),
    path('', views.index, name="home"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.CustomerProfileView , name='profile'),
    path('admin-page/', views.AdminPageView , name='admin-page')

]
# urlpatterns = [
#     path('', views.CustomerProfileView, name='profile'),
# ]
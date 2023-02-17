from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name = 'home'),
    path('authorize', views.Authorization.as_view(), name = 'authorize'), 
    path('login',views.LoginPage.as_view(), name = 'login' ),
    path('logout',views.LogoutPage.as_view(), name = 'logout'),
    path('signup',views.Signupview.as_view(),name = 'signup')
    ]

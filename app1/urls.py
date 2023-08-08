from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView


urlpatterns = [
     path('', views.SignupPage, name='signup'),
     path('login/', views.LoginPage, name='login'),
     path('home/', views.HomePage, name='home'),
     path('logout/', views.LogoutPage, name='logout'),
     path('password_reset/', views.CustomPasswordResetView.as_view(),
         name='password_reset'),
     path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(),
         name='password_reset_done'),
     #path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(),
        # name='password_reset_confirm'),
     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('reset/done/', views.CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]

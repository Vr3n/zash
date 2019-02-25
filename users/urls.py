from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from users import views as user_views
from .views import (register,
                    profile)
from . import views

# Write your url patterns Here.
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('profile/change-password', views.change_password, name='change_password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/password_reset/', auth_views.PasswordResetView, name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView, name='password_reset_done'),
    re_path('reset/<uidb64>/<token>', auth_views.PasswordResetCompleteView, name='password_reset_complete'),
]
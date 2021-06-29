from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login',LoginView.as_view(),name="login"),
    path('register/',views.registerView,name="register"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
]
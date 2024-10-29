from django.urls import path
from django.shortcuts import render
from authApp.views import ProtectedView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('',views.home_view,name='home'),
    path('accounts/login/',views.login_view,name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('home/', lambda request: render(request, 'auth1_app/home.html'), name='home'),
    path('logout-page/', lambda request: render(request, 'accounts/logout.html'), name='logout_page'),  # Logout confirmation page
    path('register/',views.register_view,name='register'),
    path('protected/',ProtectedView.as_view(),name='protected'),
]
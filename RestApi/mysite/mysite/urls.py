from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView, name='login'),
    path('accounts/logout/', views.LogoutView, name='logout'),
    path('', include('poll.urls')),
]

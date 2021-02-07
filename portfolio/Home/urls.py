from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume' ),
    path('work/', views.work, name='work'),
    path('contact', views.contact, name='contact')
]
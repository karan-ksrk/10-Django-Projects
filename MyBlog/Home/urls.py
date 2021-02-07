from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog', views.blog, name='blog'),
    path('path/<id>/', views.post, name='post'),
    path('search', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
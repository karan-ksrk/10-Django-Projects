from django.urls import path
from . import views

app_name = 'poll'
urlpatterns = [
    path('poll/', views.IndexView.as_view()),
    path('poll/<pk>/delete/', views.DeleteView.as_view(), name="delete"),
    path('poll/<pk>/', views.DetailView.as_view(), name="detail")
]
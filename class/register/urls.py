from . import views
from django.urls import path

urlpatterns = [
    path('lectures/', views.lectures),
    path('subjects/', views.subjects),
    path('', views.main_window),
]
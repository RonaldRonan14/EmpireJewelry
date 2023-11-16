from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index),
    path('home/create/', views.create),
    path('home/edit/<int:id_bip>/', views.edit),
    path('home/delete/<int:id_bip>/', views.delete),
]
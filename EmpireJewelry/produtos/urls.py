from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.index),
    path('produtos/create', views.create),
    path('produtos/edit/<int:id_produto>/', views.edit),
    path('produtos/delete/<int:id_produto>/', views.delete)
]
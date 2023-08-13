
from django.contrib import admin
from django.urls import path
from . import views
# app_name = 'bookstore'
urlpatterns = [
    path('api/', views.home_to_all_books),
    path('api/add', views.add_book),
    path('api/<int:id>', views.single_book)
]

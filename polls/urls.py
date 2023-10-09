from django.urls import path
from . import views

urlpatterns = [
    path('add_book', views.create_book, name="add_book")
]
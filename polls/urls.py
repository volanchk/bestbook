from django.urls import path
from . import views

urlpatterns = [
    path('add_topic', views.create_topic, name="add_topic"),
    path('add_book', views.create_book, name="add_book")
]
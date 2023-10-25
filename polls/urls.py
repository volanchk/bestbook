from django.urls import path
from . import views

urlpatterns = [
    path('add_topic', views.create_topic, name="add_topic"),
    path("<int:pk>/add_book/", views.add_book, name="add_book"),
    path("<int:pk>/election/", views.election, name="voices"),
    path("<int:pk>/unvote", views.un_vote, name="undo")
]

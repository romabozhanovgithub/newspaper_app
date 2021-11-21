from django.urls import path
from . import views

urlpatterns = [
    path("", views.articles, name="articles"),
    path("create/", views.article_create, name="article_create"),
    path("<int:pk>/", views.article_details, name="article_details"),
    path("<int:pk>/edit/", views.article_edit, name="article_edit"),
    path("<int:pk>/delete/", views.article_delete, name="article_delete"),
    path("comments/<int:pk>/delete/", views.comment_delete, name="comment_delete"),
]

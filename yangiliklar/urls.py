from django.urls import path, include

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("news_view", views.news_view, name="news_view")
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("article/<int:pk>", views.ArticleView.as_view(), name="article"),
    path("article/create", views.ArticleCreate.as_view(success_url="/"), name="create"),
]

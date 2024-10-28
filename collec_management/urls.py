from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("collection/<id>", views.collection, name="collection"),
    path("all/", views.collections, name="all"),
    path("new/", views.new, name="new"),
    path("delete/<id>", views.delete, name="delete"),
    path("change/<id>", views.change, name="change"),
]
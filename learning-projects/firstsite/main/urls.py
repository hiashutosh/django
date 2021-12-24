from django.urls import path
from . import views

urlpatterns = [
    path("<str:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.create, name="view"),
    # path("v1/", views.view1, name="view 1"),
]

from django.urls import path
from .views import *

urlpatterns=[
    path("",home,name="home"),
    path("add",add,name="add"),
    path("edit",edit,name="edit"),
    path("delete",delete,name="del"),
]
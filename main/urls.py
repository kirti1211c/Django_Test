from venv import create
from django.urls import path 
from . import views

urlpatterns = [
    # path("",views.index,name="index"),
    # path("v1/",views.v1,name="view 1"),
    # path("<int:id>",views.index,name="index"),
    path("",views.home,name= "home"),
    path("out/",views.out,name= "out"),
    # path("create/",views.create,name= "create"),

]
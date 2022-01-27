from django.urls import path
from . import views

app_name="Game"
urlpatterns=[
               path("",views.checkwinner,name="checkwinner"),
               
        ]
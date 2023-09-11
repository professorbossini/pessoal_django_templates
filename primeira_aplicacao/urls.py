from django.urls import path
from primeira_aplicacao import views

urlpatterns = [
    path('', views.index, name="index")
]

from django.urls import path
from .views import (
    home,
    home_premium, 
)

urlpatterns = [
    path("", home, name="home"),
    path("home/", home_premium, name="home_premium"),
]

from django.urls import path
from . import views

app_name = "myportfolio"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("details/", views.PortfolioView.as_view(), name="details"),
]
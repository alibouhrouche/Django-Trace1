from django.urls import path
from .views import login_view, logout_view

app_name = "accounts"
urlpatterns = [
    path("login/", view=login_view, name="login"),
    path("logout/", view=logout_view, name="logout"),
]
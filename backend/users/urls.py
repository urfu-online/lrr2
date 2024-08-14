from django.urls import path
from .views import (
    user_detail_view,
    user_redirect_view,
    UserProfileUpdateView
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=UserProfileUpdateView.as_view(), name="update"),
    path("user/<str:username>/", view=user_detail_view, name="detail"),
    ]
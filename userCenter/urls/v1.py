from django.urls import path
from userCenter.apis.v1 import authView

urlpatterns = [
    path("auth/", authView.Auth.as_view())
]

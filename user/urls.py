from django.contrib.auth import views, urls
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from user.views import UserLoginView, UserRegistrationForm, sign_up, UserLogoutView

include('django.contrib.auth.urls')

urlpatterns = [
    path("login/", LoginView.as_view(
        next_page="/",
        redirect_authenticated_user=False
    ), name="login"),

    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),

    path("registration/", sign_up, name="registration"),
]

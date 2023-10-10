from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("transcribe/", views.transcribe, name="transcribe"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
from django.urls import path
from rest_framework.authtoken import views as auth_view
from .views import logout_view, register_view, my_profile_api_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)


app_name = 'account'

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # path("login/", auth_view.obtain_auth_token, name='login'),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    path("my_profile/", my_profile_api_view, name="my-profile"),

]

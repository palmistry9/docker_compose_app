from django.urls import path
from .apps import UsersConfig
from .views import UserRegistrationView, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('register/', UserRegistrationView.as_view(), name='register'),
              ] + router.urls
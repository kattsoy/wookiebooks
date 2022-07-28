from django.urls import path
from .views import index, BookAPIList, BookAPIUpdate, BookAPIDestroy
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', index, name='home'),
    path('api/v1/books/', BookAPIList.as_view()),
    path('api/v1/books/<int:pk>/', BookAPIUpdate.as_view()),
    path('api/v1/booksdelete/<int:pk>/', BookAPIDestroy.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
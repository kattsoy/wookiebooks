from django.urls import path
from .views import index, BookAPIList, BookApiRetrive

urlpatterns = [
    path('', index, name='home'),
    path('api/v1/books/', BookAPIList.as_view()),
    path('api/v1/books/<int:pk>/', BookApiRetrive.as_view()),
]
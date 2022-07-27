from django.urls import path
from .views import index, BookAPIList, BookAPIUpdate, BookAPIDestroy

urlpatterns = [
    path('', index, name='home'),
    path('api/v1/books/', BookAPIList.as_view()),
    path('api/v1/books/<int:pk>/', BookAPIUpdate.as_view()),
    path('api/v1/booksdelete/<int:pk>/', BookAPIDestroy.as_view()),
]
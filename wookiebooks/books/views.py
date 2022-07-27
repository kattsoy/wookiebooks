from django.shortcuts import render
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer

# Create your views here.
def index(request):
    return render(request, 'books/index.html', {})

class BookAPIList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookApiRetrive(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
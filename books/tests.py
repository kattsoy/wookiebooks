from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import User, Book


class TestCaseBookAPIList(APITestCase):
    def create_test_user(self):
        self.user = User.objects.create_user(author_pseudonym='testuser', email='test@user.com', password='password')

    def authenticate(self):
        self.create_test_user()
        response = self.client.post(reverse('token_obtain_pair'), {'email':'test@user.com', 'password':'password'})
        self.client.credentials (HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_not_creates_book(self):
        sample_book = {'title': 'TestBook', 'price': '400', 'description': "Best Test Book"}
        response = self.client.post(reverse('books'), sample_book)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_creates_book(self):
        previous_book_count = Book.objects.all().count()
        self.authenticate()
        sample_book = {'title': 'TestBook', 'price': '400','description': "Best Test Book"}
        response = self.client.post(reverse('books'), sample_book)
        self.assertEqual(Book.objects.all().count(), previous_book_count +1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

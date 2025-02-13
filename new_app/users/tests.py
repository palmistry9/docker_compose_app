from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com',
        )

    def test_registration(self):
        response = self.client.post('/api/register/', {
            'username': 'newuser',
            'password': 'newpassword',
            'email': 'new@example.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        response = self.client.get('/api-auth/login/', {
            'username': 'newuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
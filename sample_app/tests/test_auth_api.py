from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


UserModel = get_user_model()


class AuthApiTest(APITestCase):
    def test_register(self):
        payload = {"email": "new@example.com", "password": "password123"}

        response = self.client.post("/api/v1/auth/register/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["email"], "new@example.com")
        self.assertNotIn("password", response.data)
        self.assertTrue(UserModel.objects.filter(email="new@example.com").exists())

    def test_login(self):
        UserModel.objects.create_user(email="alice@example.com", password="password123")

        payload = {"email": "alice@example.com", "password": "password123"}
        response = self.client.post("/api/v1/auth/login/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_requires_login(self):
        response = self.client.post("/api/v1/auth/logout/", {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logout_after_login(self):
        user = UserModel.objects.create_user(email="alice@example.com", password="password123")
        self.client.force_login(user)

        response = self.client.post("/api/v1/auth/logout/", {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

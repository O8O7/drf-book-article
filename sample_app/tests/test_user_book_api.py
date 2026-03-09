from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from sample_app.models import BookModel, UserBookModel


UserModel = get_user_model()


class UserBookApiTest(APITestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(email="alice@example.com", password="password123")
        self.other_user = UserModel.objects.create_user(email="bob@example.com", password="password123")
        self.book1 = BookModel.objects.create(title="Django入門", author="田中一郎")
        self.book2 = BookModel.objects.create(title="DRF実装ガイド", author="佐藤花子")

    def test_requires_authentication(self):
        response = self.client.get("/api/v1/user-books/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_only_my_user_books(self):
        UserBookModel.objects.create(user=self.user, book=self.book1, status="unread")
        UserBookModel.objects.create(user=self.other_user, book=self.book2, status="reading")

        self.client.force_login(self.user)
        response = self.client.get("/api/v1/user-books/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["book"], self.book1.id)

    def test_create_user_book_sets_current_user(self):
        self.client.force_login(self.user)

        payload = {
            "user": self.other_user.id,
            "book": self.book1.id,
            "status": "reading",
            "memo": "メモ",
        }
        response = self.client.post("/api/v1/user-books/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user_book = UserBookModel.objects.get(id=response.data["id"])
        self.assertEqual(user_book.user_id, self.user.id)

    def test_update_my_user_book(self):
        user_book = UserBookModel.objects.create(user=self.user, book=self.book1, status="unread")

        self.client.force_login(self.user)
        response = self.client.patch(
            f"/api/v1/user-books/{user_book.id}/",
            {"status": "finished", "memo": "読了"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_book.refresh_from_db()
        self.assertEqual(user_book.status, "finished")
        self.assertEqual(user_book.memo, "読了")

    def test_cannot_update_other_users_user_book(self):
        other_user_book = UserBookModel.objects.create(user=self.other_user, book=self.book2, status="reading")

        self.client.force_login(self.user)
        response = self.client.patch(
            f"/api/v1/user-books/{other_user_book.id}/",
            {"status": "finished"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

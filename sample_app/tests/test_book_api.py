from rest_framework import status
from rest_framework.test import APITestCase

from sample_app.models import BookModel


class BookApiTest(APITestCase):
    def test_list_books(self):
        BookModel.objects.create(title="Django入門", author="田中一郎")
        BookModel.objects.create(title="DRF実装ガイド", author="佐藤花子")

        response = self.client.get("/api/v1/books/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 2)

    def test_retrieve_book(self):
        book = BookModel.objects.create(title="Python実践入門", author="山田太郎")

        response = self.client.get(f"/api/v1/books/{book.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], book.id)
        self.assertEqual(response.data["title"], "Python実践入門")
        self.assertEqual(response.data["author"], "山田太郎")

    def test_create_book_is_not_allowed(self):
        payload = {
            "title": "新規作成したい本",
            "author": "著者名",
        }

        response = self.client.post("/api/v1/books/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_book_is_not_allowed(self):
        book = BookModel.objects.create(title="古いタイトル", author="田中一郎")

        response = self.client.patch(
            f"/api/v1/books/{book.id}/",
            {"title": "新しいタイトル"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_book_is_not_allowed(self):
        book = BookModel.objects.create(title="削除対象", author="田中一郎")

        response = self.client.delete(f"/api/v1/books/{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

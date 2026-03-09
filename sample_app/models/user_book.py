from django.conf import settings
from django.db import models


class ReadingStatus(models.TextChoices):
    """読書ステータス定義"""

    UNREAD = "unread", "未読"
    READING = "reading", "読書中"
    FINISHED = "finished", "読了"


class UserBookModel(models.Model):
    """ユーザーと書籍の中間モデル"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="ユーザー",
        on_delete=models.CASCADE,
        related_name="user_books",
    )
    book = models.ForeignKey(
        "sample_app.BookModel",
        verbose_name="書籍",
        on_delete=models.CASCADE,
        related_name="user_books",
    )
    status = models.CharField("読書ステータス", max_length=20, choices=ReadingStatus.choices, default=ReadingStatus.UNREAD)
    memo = models.TextField("メモ", blank=True, default="")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        db_table = "user_books"
        verbose_name = "ユーザー書籍"
        verbose_name_plural = "ユーザー書籍一覧"
        constraints = [
            models.UniqueConstraint(fields=["user", "book"], name="unique_user_book"),
        ]

    def __str__(self) -> str:
        """管理画面向けの表示名"""
        return f"{self.user} - {self.book} ({self.status})"

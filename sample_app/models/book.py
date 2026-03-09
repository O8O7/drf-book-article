from django.db import models


class BookModel(models.Model):
    """書籍を表すモデル。"""

    title = models.CharField("タイトル", max_length=255)
    author = models.CharField("著者", max_length=255)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        db_table = "books"
        verbose_name = "書籍"
        verbose_name_plural = "書籍一覧"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        """管理画面向けの表示名"""
        return f"{self.title} / {self.author}"

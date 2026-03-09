from __future__ import annotations

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager["UserModel"]):
    """メールアドレス認証用のユーザーマネージャ。"""

    use_in_migrations = True

    def create_user(self, email: str, password: str | None = None, **extra_fields: object) -> "UserModel":
        """通常ユーザーを作成する

        Args:
            email: ログインに利用するメールアドレス
            password: 平文パスワード
            **extra_fields: 追加のユーザー属性

        Returns:
            作成されたユーザー
        """
        if not email:
            raise ValueError("メールアドレスは必須です。")

        normalized_email = self.normalize_email(email)
        user = self.model(email=normalized_email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields: object) -> "UserModel":
        """スーパーユーザーを作成する

        Args:
            email: ログインに利用するメールアドレス
            password: 平文パスワード
            **extra_fields: 追加のユーザー属性

        Returns:
            作成されたユーザー
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email=email, password=password, **extra_fields)


class UserModel(AbstractUser):
    """email/passwordで認証を行うカスタムユーザーモデル"""

    # 今回のサンプルプロジェクトはusername, first_name, last_nameは不要なカラムのためNoneにする
    username = None 
    first_name = None
    last_name = None

    email = models.EmailField("メールアドレス", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = "ユーザー"
        verbose_name_plural = "ユーザー一覧"


    def __str__(self) -> str:
        return self.email

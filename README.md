# 概要

本リポジトリは、以下の技術記事で紹介しているサンプルコードとして作成しています。

> 技術記事 📖 ->
[DjangoRestFrameworkでAPI構築してみよう](https://qiita.com/shun_sakamoto/items/02cd9c20234510191a3f)

主な機能

- ユーザー登録 / ログイン / ログアウト
- 書籍一覧取得
- ユーザーごとの読書状態管理
- Django Adminによるデータ管理


# データ構造

以下の3テーブルで構成されています。

| Table      | Description    |
| ---------- | -------------- |
| users      | ユーザー           |
| books      | 書籍マスタ          |
| user_books | ユーザーごとの読書ステータス |

ER図

![ER図](docs/db_er.svg)

# API一覧

## 認証API

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | /api/v1/auth/register/ |
| POST   | /api/v1/auth/login/    |
| POST   | /api/v1/auth/logout/   |

## 書籍API

| Method | Endpoint            |
| ------ | ------------------- |
| GET    | /api/v1/books/      |
| GET    | /api/v1/books/{id}/ |

## 読書管理API

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | /api/v1/user-books/      |
| POST   | /api/v1/user-books/      |
| GET    | /api/v1/user-books/{id}/ |
| PUT    | /api/v1/user-books/{id}/ |
| PATCH  | /api/v1/user-books/{id}/ |
| DELETE | /api/v1/user-books/{id}/ |

# セットアップ

## 仮想環境作成

```bash
python -m venv venv
```

Linux / Mac

```bash
source ./venv/bin/activate
```

Windows

```bash
.\venv\Scripts\activate
```

## ライブラリインストール

```bash
pip install -r requirements.txt
```

## マイグレーション

```bash
python manage.py migrate
```

## 管理ユーザー作成

```bash
python manage.py createsuperuser
```

## サーバー起動

```bash
python manage.py runserver
```

# API確認
ブラウザから以下にアクセスするとDRFのAPIブラウザで確認できます。

```
http://127.0.0.1:8000/api/v1/
```

# 管理画面
```
http://127.0.0.1:8000/admin/
```

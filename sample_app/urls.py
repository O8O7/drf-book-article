from django.urls import path
from rest_framework.routers import DefaultRouter

from sample_app.views.auth import LoginAPIView, LogoutAPIView, RegisterAPIView
from sample_app.views.book import BookViewSet
from sample_app.views.user_book import UserBookViewSet

router = DefaultRouter()
router.register("books", BookViewSet, basename="books")
router.register("user-books", UserBookViewSet, basename="user-books")

urlpatterns = [
    path("auth/register/", RegisterAPIView.as_view(), name="auth-register"),
    path("auth/login/", LoginAPIView.as_view(), name="auth-login"),
    path("auth/logout/", LogoutAPIView.as_view(), name="auth-logout"),
]
urlpatterns += router.urls

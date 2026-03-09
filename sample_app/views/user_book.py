from rest_framework import permissions, viewsets

from sample_app.models import UserBookModel
from sample_app.serializers.user_book import UserBookSerializer


class UserBookViewSet(viewsets.ModelViewSet):
    serializer_class = UserBookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # ログイン中であるユーザー自身のデータだけ返す
        return UserBookModel.objects.filter(user=self.request.user).select_related("book", "user").order_by("-updated_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import serializers

from sample_app.models import UserBookModel


class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookModel
        fields = [
            "id",
            "user",
            "book",
            "status",
            "memo",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

from rest_framework import serializers

from sample_app.models import BookModel


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ["id", "title", "author", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

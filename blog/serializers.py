from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ("id", "title", "content", "author", "published_date", "slug")
        read_only_fields = ("author", "published_date")
        lookup_field = "id"
        extra_kwargs = {
            "url": {"lookup_field": "id"},
        }

    def get_author(self, obj):
        return obj.author.username if obj.author else None

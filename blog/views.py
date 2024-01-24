from rest_framework import generics, permissions

from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        else:
            return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return []
        else:
            return [permissions.IsAuthenticated()]

    def get_queryset(self):
        if self.request.method == "GET":
            return BlogPost.objects.all()
        else:
            return BlogPost.objects.filter(author=self.request.user)

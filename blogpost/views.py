from django.http import Http404
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from drf_pp5_api.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class BlogPostList(generics.ListCreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = BlogPost.objects.annotate(
        likes_count=Count('likes', distinct=True),
        bookmarks_count=Count('bookmark', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'bookmarks_count',
        'likes__created_at',
    ]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request):
        posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = BlogPost.objects.annotate(
        likes_count=Count('likes', distinct=True),
        bookmarks_count=Count('bookmark', distinct=True)
    ).order_by('-created_at')
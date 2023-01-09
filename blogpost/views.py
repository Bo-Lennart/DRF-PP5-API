from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from drf_pp5_api.permissions import IsOwnerOrReadOnly


class BlogPostList(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

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


class BlogPostDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BlogPostSerializer

    def get_object(self, pk):
        try:
            post = BlogPost.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except BlogPost.DoesNotExist:
            raise Http404 

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = BlogPostSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = BlogPostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, statuts=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
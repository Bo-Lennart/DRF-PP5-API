from rest_framework import generics, permissions
from drf_pp5_api.permissions import IsOwnerOrReadOnly
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
    """
    get Bookmark or delete if owner of the Bookmark
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()
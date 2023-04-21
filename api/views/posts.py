from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from api.permissions import IsAllowed
from api.serializers import PostSerializer
from posts.models import Post


class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAllowed]
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class.account = request.user
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Post, pk=pk)
        _serializer = self.serializer_class(instance, data=request.data)
        if _serializer.is_valid():
            _serializer.save()
            return Response(_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

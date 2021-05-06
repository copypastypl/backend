from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer

class PostView(ModelViewSet):
    serializer_class = PostSerializer

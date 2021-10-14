from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, UserDetailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserDetailView(APIView):
    "Return user data from token"
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)
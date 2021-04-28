import jwt
import datetime

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.conf import settings

from .serializers import UserSerializer, UserDetailSerializer
from .models import User
from .authentication import JWTAuthentication


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        data = UserDetailSerializer(request.user).data
        return Response(data)


class UserLoginView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, username=data['username'])
        print(datetime.datetime.now() + datetime.timedelta(seconds=30))
        payload = {
            'user_id': user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return Response({'jwt_token': jwt_token})

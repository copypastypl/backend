from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer
from .models import User


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

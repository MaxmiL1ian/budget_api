from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .models import User
from .serializers import UserSerializer


class UserAPIView(APIView):

    def get(self, request):
        try:
            login = User.objects.get(login=request.data['login'])
            password = User.objects.get(password=request.data['password'])
        except:
            login = None
            password = None

        if login is None and password is None:
            raise ValidationError

        return Response({"data": UserSerializer(
            User.objects.get(login=request.data['login'], password=request.data['password'])).data})

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid(raise_exception=True):
            User.objects.create(
                first_name=user.data.get("first_name"),
                last_name=user.data.get("last_name"),
                login=user.data.get("login"),
                password=user.data.get("password")

            )
            return Response({"data": user.data})

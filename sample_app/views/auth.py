from django.contrib.auth import authenticate, get_user_model, login, logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from sample_app.serializers.auth import LoginSerializer, RegisterSerializer


UserModel = get_user_model()


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        response_data = {
            "id": user.id,
            "email": user.email,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        if user is None:
            return Response({"detail": "メールアドレスまたはパスワードが正しくありません。"}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"detail": "ログインしました。"}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"detail": "ログアウトしました。"}, status=status.HTTP_200_OK)

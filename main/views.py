from django.shortcuts import render
from .serializers import *
from rest_framework.generics import *
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
# Create your views here.
class HeaderView(ListCreateAPIView,UpdateAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class CategoryView(ListCreateAPIView,UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryView(ListCreateAPIView,UpdateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class CardView(ListCreateAPIView,UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)
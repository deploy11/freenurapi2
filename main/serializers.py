from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user_obj = User.objects.create_user(email=validated_data.get('email'), username=validated_data.get('username'), password=validated_data.get('password'))
        return user_obj

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
       model = Header
       fields = ('id','bg','title','btn')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = Category
       fields = ('id','name')

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = Card
       fields = ('id','name','category','image')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
       model = Card
       fields = ('id','subcategory','image','title','prrce','details')
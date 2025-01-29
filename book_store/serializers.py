from rest_framework import serializers
from .models import User,Book
from django.contrib.auth.hashers import make_password


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["book_name","book_title","price","quantity","author","description","published_at"]

class Registration(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=6,style={"input_type":"password"})
    confirm_password = serializers.CharField(write_only=True,min_length=6,style={"input_type":"password"})

    class Meta:
        model = User
        fields = ['username','password','confirm_password','email','user_type','is_active','created_at']


    def validate(self,data):
        password = data.get("password")
        confirm_password = data.pop("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError("Password Not Matched !")
        else:
            data['password'] = make_password(password)
            return data
        


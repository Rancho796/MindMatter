from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, vaildated_data):
        # create a user with a hashed password
        user = User.objects.create_user(
            username=vaildated_data["username"],
            password=vaildated_data["password"],
        )
        return user

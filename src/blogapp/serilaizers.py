from rest_framework import serializers
from commentapp.models import Blog,Comment
# from .models import Blog
from userapp.serilaizer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id","text","user","created_at"]
        read_only_fileds=["id","user","created_at"]

class BlogSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    creator = UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ["id","title", "description", "image", "creator","comments"]
        read_only_fileds=["id","creator"]


    def create(self, validated_data):
        # Get the user from the request object  (JWT token is decoded automatically)
        user = self.context["request"].user
        # create a new blog  and set creator filed to the current user
        blog = Blog.objects.create(creator=user, **validated_data)
        return blog

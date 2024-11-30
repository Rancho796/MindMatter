from rest_framework import serializers
from .models import Comment
from blogapp.serilaizers import UserSerializer,BlogSerializer
from blogapp.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Blog
        fields = ["id","title", "description", "image", "creator"]
        read_only_fileds=["id","creator"]

class CommentSerializer(serializers.ModelSerializer):
    blog_id=serializers.IntegerField(write_only=True)
    blog=BlogSerializer(read_only=True)
    user=UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id","text","blog_id","user","created_at","blog"]
        read_only_fileds=["id","user","created_at","blog"]

    def create(self, validated_data):
    # Get the user from the request object  (JWT token is decoded automatically)
        user = self.context["request"].user

        blog_id=validated_data.pop('blog_id')
        try:
           blog=Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            raise serializers.ValidationError({'blog_id':'Blog does not exist.'})
        
        # create a new blog  and set creator filed to the current user
        # blog = Blog.objects.create(creator=user, **validated_data)
        # return blog
        return Comment.objects.create(user=user,blog=blog,**validated_data)

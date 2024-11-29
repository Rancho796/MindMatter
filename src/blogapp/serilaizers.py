from rest_framework import serializers
from .models import  Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['title','description','image','creator']
        
    def create(self, validated_data):
       #Get the user from the request object  (JWT token is decoded automatically)
       user=self.context['request'].user
       #create a new blog  and set creator filed to the current user
       blog=Blog.objects.create(creator=user,**validated_data)
       return blog

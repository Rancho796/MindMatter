from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Comment
from .serializers import CommentSerializer
# Create your views here.

class CreateAndGetAllComment(ListCreateAPIView):
    queryset=Comment.objects.select_related("user","blog")
    serializer_class=CommentSerializer

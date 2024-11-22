from django.shortcuts import render
# from django.http import JsonResponse
# import json
from .models import *
from .serilaizers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# blogs = {
#     1: {
#         "id": 1,
#         "title": "python",
#         "description": "python is high level programming language which is use for general pusrpose.",
#     },
#     2: {
#         "id": 2,
#         "title": "java",
#         "description": "java is based on oops and its high level programming language.",
#     },
# }


# @csrf_exempt
# @api_view(["GET", "POST"])
# class CreateAndGetAllBlogs(APIView):
#     # if request.method == "GET":
#     def get(self,request):
#         blogs=Blog.objects.all().values()
#         # return JsonResponse({"blogs": list(blogs)}, safe=False)
#         serializer=BlogSerializer(blogs,many=True)
#         return Response({"blogs":serializer.data})
    
#     def post(self,request):
#         serializer=BlogSerializer(data=request.data)
#         if(serializer.is_valid()):
#             serializer.save()
#             return Response({
#                 "message":"Blog created successfully.","blogs":serializer.data
#             },status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class GetUpdateaDeleteBlog(APIView):
#     def getBlog(self,id):
#         try:
#             return Blog.objects.get(id=id)
#         except Blog.DoesNotExist:
#             return None
#         # return JsonResponse({"error":"blog not found"},status=204)
#     # blog = blogs.get(id)

#     def get(self,request,id):
#         blog=self.getBlog(id)
#         if(blog is None):
#             return Response({"error":"Blog not found"},status=status.HTTP_404_NOT_FOUND)
#         serializer=BlogSerializer(blog)
#         return Response({"id":serializer.data})
#         # return JsonResponse({"blog":{"id":blog.id,"title":blog.title,"description":blog.description}})

#     def put(self,request,id):
#         blog=self.getBlog(id)
#         if(blog is None):
#             return Response({"error":"blog is not found."},status=status.HTTP_404_NOT_FOUND)
        
#         serializer=BlogSerializer(blog,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"Blog updated successfully","blog":serializer.data})
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,id):
#         blog=self.getBlog(id)
#         if(blog is None):
#             return Response({"error":"Blog not found"},status=status.HTTP_404_NOT_FOUND)
#         # del blogs[id]
#         blog.delete()
#         # return JsonResponse({"message": "Blog deleted successfully"}, status=204)
#         return Response({"message":"blog deleted successfully"},status=status.HTTP_204_NO_CONTENT)

class CreateAndGetAllBlogs(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class GetUpdateDeleteBlog(RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

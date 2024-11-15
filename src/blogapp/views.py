from django.shortcuts import render
# from django.http import JsonResponse
# import json
from .models import *
from .serilaizers import BlogSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


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


@csrf_exempt
@api_view(["GET", "POST"])
def createAndGetAllBlogs(request):
    if request.method == "GET":
        blogs=Blog.objects.all().values()
        # return JsonResponse({"blogs": list(blogs)}, safe=False)
        serializer=BlogSerializer(blogs,many=True)
        return Response({"blogs":serializer.data})
    elif request.method == "POST":
        # data = json.loads(request.body)
        # new_blog=Blog(title=data.get("title"),description=data.get("description"))
        # new_blog.save()
        # new_id = max(blogs.keys()) + 1
        # print(data)
        # type(data)
        # new_blog = {
        #     "id": new_id,
        #     "title": data.get("title"),
        #     "description": data.get("description"),
        # }
        # blogs[new_id] = new_blog
        # return JsonResponse(
        #     {"message": "blog created successfully", "blog": {"id":new_blog.id,"title":new_blog.title,"description":new_blog.description}}, status=201
        # )
        serializer=BlogSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "message":"Blog created successfully.","blogs":serializer.data
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getUpdateaDeleteBlog(request, id):
    try:
        blog=Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return Response({"error":"blog not found"},status=status.HTTP_404_NOT_FOUND)
        # return JsonResponse({"error":"blog not found"},status=204)
    # blog = blogs.get(id)

    if request.method == "GET":
        serializer=BlogSerializer(blog)
        return Response({"id":serializer.data})
        # return JsonResponse({"blog":{"id":blog.id,"title":blog.title,"description":blog.description}})

    elif request.method == "PUT":
        # data = json.loads(request.body)
        # blog.title=data.get("title",blog.title)
        # blog.description=data.get("description",blog.description)
        # blog.save()
        # blog.update(
        #     {"title": data.get("title"), "description": data.get("description")}
        # )
        # return JsonResponse({"message": "Blog updated successfully", "blog":{
        #     "id":blog.id,
        #     "title":blog.title,
        #     "description":blog.description
        # } })
        serializer=BlogSerializer(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Blog updated successfully","blog":serializer.data})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        # del blogs[id]
        blog.delete()
        # return JsonResponse({"message": "Blog deleted successfully"}, status=204)
        return Response({"message":"blog deleted successfully"},status=status.HTTP_204_NO_CONTENT)

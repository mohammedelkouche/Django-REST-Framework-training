from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#class-based Views
#------ APIView class for working with class-based views -------
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class   PostsAPIViews(APIView):
    def get(self, request):
        posts = Post.objects.all() #querySet
        serialazer = PostSerializer(posts, many=True)
        return Response(serialazer.data)

    def post(self, request):
        serialazer = PostSerializer(data = request.data)
        
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data, status=status.HTTP_201_CREATED)
        return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class posts_detailsAPIViews(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        




#------ @api_view decorator for working with function based views -------


# @api_view(['GET', 'POST'])
# def PostsView(request):

#     if request.method == 'GET':
#         posts = Post.objects.all() #querySet
#         #if you have fecth all the data fome the table (querySet) use many=True
#         serialazer = PostSerializer(posts, many=True)
#         return Response(serialazer.data)
    
#     elif request.method == 'POST':
#         serialazer = PostSerializer(data = request.data)
        
#         if serialazer.is_valid():
#             serialazer.save()
#             return Response(serialazer.data, status=status.HTTP_201_CREATED)
#         return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

# #pk : primary kay 
# # we can pass id instead of pk
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def posts_detail(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)  # instanse
#     except post.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT': #update
#         serializer = PostSerializer(post, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
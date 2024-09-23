from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def PostsView(request):

    if request.method == 'GET':
        posts = Post.objects.all() #querySet
        #if you have fecth all the data fome the table (querySet) use many=True
        serialazer = PostSerializer(posts, many=True)
        return Response(serialazer.data)
    
    elif request.method == 'POST':
        serialazer = PostSerializer(data = request.data)
        
        if serialazer.is_valid():
            serialazer.save()
            return Response(serialazer.data, status=status.HTTP_201_CREATED)
        return Response(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

#pk : primary kay 
# we can pass id instead of pk
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def posts_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)  # instanse
    except post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT': #update
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
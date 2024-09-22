from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.

def PostsView(request):

    if request.method == 'GET':
        posts = Post.objects.all() #querySet
        #if you have fecth all the data fome the table (querySet) use many=True
        serialazer = PostSerializer(posts, many=True)
        return JsonResponse(serialazer.data, safe =False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serialazer = PostSerializer(data = data)
        
        if serialazer.is_valid():
            serialazer.save()
            return JsonResponse(serialazer.data, status=201)
        return JsonResponse(serialazer.errors, status=400)
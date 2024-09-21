from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser


# Create your views here.

def Posts(request):

    if request.method == 'GET':
        posts = Post.objects.all() #querySet
        #if you have fecth all the data fome the table querySet use many=True
        serialaze = PostSerializer(Post, many=True)
        return JsonResponse(serialaze.data, safe =False)

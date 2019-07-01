from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import Category, News
from blog.serializers import CategorySerializer, NewsSerializer


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "hello world"})

@api_view(["GET"])
def categories(request):
    quaryset = Category.objects.all()
    serialized = CategorySerializer(quaryset, many=True)
    return Response(serialized.data)

@api_view(["GET"])
def news(request):
    quaryset = News.objects.all()
    serialized = NewsSerializer(quaryset, many=True)
    return Response(serialized.data)

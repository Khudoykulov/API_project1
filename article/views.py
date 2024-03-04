from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def article_list(request):
    qs = Article.objects.all()
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def article_detail(request, pk):
    obj = get_object_or_404(Article, id=pk)
    serializer = ArticleSerializer(obj)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
# @authentication_classes([BasicAuthentication])
def article_create(request):
    context = {
        "user_id": request.user.id
    }
    serializer = ArticleSerializer(data=request.data, context=context)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    response = {
        "message": serializer.errors
    }
    return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def list_create_view(request):
    if request.method == "POST":
        context = {
            "user_id": request.user.id
        }
        serializer = ArticleSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        response = {
            "error": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    qs = Article.objects.all()
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def my_articles_view(request):
    qs = Article.objects.filter(author=request.user)
    serializer = ArticleSerializer(qs, many=True)
    return Response(serializer.data)

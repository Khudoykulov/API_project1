from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .serializers import TagSerializer, RecipeSerializer, IngredientSerializer, RecipePostSerializer
from rest_framework.views import APIView
from .models import Tag, Recipe, Ingredient
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from .permissions import IsAuthorOrReadOnly


class TagAPIView(APIView):

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['title',],
            example={
                'title': 'title'
            }
        ),
        responses={201: "Created", 400: "Bad Request"},
    )
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = TagSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class TagDetailAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=200)


class TagUpdateAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['title',],
            example={
                'title': 'title'
            }
        ),
        responses={201: "Created", 400: "Bad Request"},
    )
    def put(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(instance=tag, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class TagDeleteAPIView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        tag.delete()
        return Response(status=204)


class TagPartialUpdateAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['title',],
            example={
                'title': 'title'
            }
        ),
        responses={201: "Created", 400: "Bad Request"},
    )
    def patch(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(instance=tag, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class TagRUDAPIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['title',],
            example={
                'title': 'title'
            }
        ),
        responses={201: "Created", 400: "Bad Request"},
    )
    def patch(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(instance=tag, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        tag.delete()
        return Response(status=204)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type="object",
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING,),
            },
            required=['title',],
            example={
                'title': 'title'
            }
        ),
        responses={201: "Created", 400: "Bad Request"},
    )
    def put(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(instance=tag, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request, pk, *args, **kwargs):
        tag = get_object_or_404(Tag, id=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=200)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]


class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated,]
    # parser_classes = [MultiPartParser]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RecipeSerializer
        return RecipePostSerializer


class RecipeRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthorOrReadOnly,]
    lookup_field = 'slug'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'delete'}, status=status.HTTP_204_NO_CONTENT)


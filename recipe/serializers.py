from rest_framework import serializers
from account.serializers import UserSerializer2
from .models import (
    Tag,
    Recipe,
    Ingredient
)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'slug', 'author', 'image', 'description', 'tags', 'created_date']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'recipe', 'title', 'unit', 'quantity', 'is_active']



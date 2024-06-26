from rest_framework import serializers
from account.serializers import UserSerializer2
from .models import (
    Tag,
    Recipe,
    Ingredient
)
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class RecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer2(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'slug', 'author', 'image', 'description', 'tags', 'created_date']


class RecipePostSerializer(serializers.ModelSerializer):
    author = UserSerializer2(read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'slug', 'author', 'image', 'description', 'tags', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        user_id = request.user.id
        validated_data['author_id'] = user_id
        return super().create(validated_data)


class IngredientSerializer(serializers.ModelSerializer):
    unit_name = serializers.CharField(source='get_unit_display', read_only=True)

    class Meta:
        model = Ingredient
        fields = ['id', 'title', 'unit_name', 'unit', 'quantity', 'is_active']

    def validate(self, attrs):
        recipe_id = self.context.get('recipe_id')
        recipe = get_object_or_404(Recipe, id=recipe_id)
        if recipe.author_id != self.context['request'].user.id:
            raise ValidationError({'author_id': 'You do not have permission to!!!'})
        return attrs

    def create(self, validated_data):
        recipe_id = self.context.get('recipe_id')
        validated_data['recipe_id'] = recipe_id
        return super().create(validated_data)




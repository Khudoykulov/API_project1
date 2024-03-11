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
    class Meta:
        model = Ingredient
        fields = ['id', 'recipe', 'title', 'unit', 'quantity', 'is_active']



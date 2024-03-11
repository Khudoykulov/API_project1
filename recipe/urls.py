from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe.views import (
    TagAPIView,
    TagDetailAPIView,
    TagUpdateAPIView,
    TagDeleteAPIView,
    TagPartialUpdateAPIView,
    TagRUDAPIView,
    TagViewSet,
    RecipeListCreateAPIView,
    RecipeRUDAPIView
)
app_name = 'recipe'

router = DefaultRouter()
router.register('tags', TagViewSet, basename='recipe')

urlpatterns = [
    # path('tag-list-create/', TagAPIView.as_view(), name='tag-list-create'),
    # path('tag-detail/<int:pk>/', TagDetailAPIView.as_view(), name='tag-detail'),
    # path('tag-update/<int:pk>/', TagUpdateAPIView.as_view(), name='tag-update'),
    # path('tag-delete/<int:pk>/', TagDeleteAPIView.as_view(), name='tag-delete'),
    # path('tag-partial-update/<int:pk>/', TagPartialUpdateAPIView.as_view(), name='tag-partial-update'),
    # path('tag-rud/<int:pk>/', TagRUDAPIView.as_view(), name='tag-rud'),
    path('', include(router.urls)),
    path('list-create/', RecipeListCreateAPIView.as_view(), name='list-create'),
    path('list-rud/<slug:slug>/', RecipeRUDAPIView.as_view(), name='list-rud'),



]

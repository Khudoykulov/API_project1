from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    list_create_view,
    my_articles_view,
    article_delete_api_view,
    article_update_api_view,
    article_update_detail_delete_api_view,
)

app_name = 'article'

urlpatterns = [
    path('list/', article_list, name='list'),
    path('detail/<int:pk>/', article_detail, name='detail'),
    path('create/', article_create, name="create"),
    path("list-create/", list_create_view, name="list-create"),
    path("my_articles/", my_articles_view, name="my_articles"),
    path("update/<int:pk>/", article_update_api_view, name="update"),
    path("delete/<int:pk>/", article_delete_api_view, name="delete"),
    path("detail-update-delete/<int:pk>/", article_update_detail_delete_api_view, name="detail-update-delete"),
]

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to="articles/", null=True, blank=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.id, filename)

class Article(models.Model): 
    title= models.CharField(max_length=255)   
    body= models.TextField()
    cover = models.ImageField(upload_to=user_directory_path)
    date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])

class CommentPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField("Текст комментария", max_length=500)
    def __str__(self):
        return self.comment
    def get_absolute_url(self):
        return reverse('article_detail')
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=50, default='General')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    edited = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='threads', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

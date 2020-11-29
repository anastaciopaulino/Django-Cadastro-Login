from django.db import models
from django.utils.text import slugify


from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    summary = models.CharField(max_length=450)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


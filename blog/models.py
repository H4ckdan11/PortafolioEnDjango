from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/images')
    updated_at = models.DateTimeField(datetime.date.today)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
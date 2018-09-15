from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=450)
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)     #create time
    updated_at = models.DateTimeField(auto_now_add=True)     #update time

    def __str__(self):
        return self.title
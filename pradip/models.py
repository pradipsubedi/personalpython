from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    pic = models.ImageField(upload_to='blogs/', null=True, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# class Contact(models.Model):
#     c_name = models.CharField(max_length=100)
#     c_subject = models.CharField(max_length=500)
#     c_message = models.TextField()
#     c_email = models.EmailField()
#     c_time = models.DateTimeField(auto_now_add=True, db_index=True)

#     def __str__(self):
#         return 'Message for {}'.format(self.sender)

class Album(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    pic = models.ImageField(upload_to='albums/', null=True, blank=False)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, null=True, blank=True, related_name='album')
    pic = models.ImageField(upload_to='gallery/', null=True, blank=False)

    def __str__(self):
        return self.album.name

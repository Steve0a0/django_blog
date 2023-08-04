from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NewPost(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    publication_time = models.DateTimeField(null=True, blank=True)
    categories = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blog')
    
    def __str__(self):
        return self.title + '|' + str(self.author)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aboutme= models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username


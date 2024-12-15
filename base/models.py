from contextlib import nullcontext
from email.policy import default
from operator import mod
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User


# from django.db import models
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    videotitle = models.CharField(max_length=800,default=None)
    video = EmbedVideoField()  # same like models.URLField()

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null= True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null= True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User,related_name='participants',blank= True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
        
    def __str__(self):
        return self.body[0:50]
    
    
    
## trial of the user profile section 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    job_role = models.CharField(max_length=255, blank=True, null=True)
    personal_details = models.TextField(blank=True,null=True)
    def get_interests(self):
        # Extract topics from personal_details and return them as a list
        return [topic.strip() for topic in self.personal_details.split(',')] if self.personal_details else []


from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
    @property
    def get_video_url(self):
        return self.video_file.url
    

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    description = models.TextField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)  # New field for public/private

    def __str__(self):
        visibility = "Public" if self.is_public else "Private"
        return f"{self.user.username}'s {visibility} Document - {self.file.name}"
    
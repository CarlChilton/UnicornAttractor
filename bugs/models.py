from django.db import models
from django.utils import timezone

class Bug(models.Model):
    """
    A single Blog posts
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="Not seen")
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    """
    A single Blog posts
    """
    id = models.AutoField(primary_key=True)
    bugId = models.IntegerField()
    featureId = models.IntegerField()
    contents = models.TextField()
    user = models.TextField(default="unknown")
    created_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title
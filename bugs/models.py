from django.db import models
from django.utils import timezone

class Bug(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default="To do")
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    bug = models.ForeignKey(Bug, related_name="bug")
    featureId = models.IntegerField()
    contents = models.TextField()
    user = models.TextField(default="unknown")
    created_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

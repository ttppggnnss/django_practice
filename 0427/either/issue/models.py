from django.db import models

# Create your models here.
class Issue(models.Model):
    nameA = models.CharField(max_length = 20)
    nameB = models.CharField(max_length = 20)
    hitcountA = models.IntegerField()
    hitcountB = models.IntegerField()

class Reply(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    pick = models.CharField(max_length = 2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
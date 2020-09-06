from django.db import models

# Create your models here.
class Reservation(models.Model):
    date = models.DateField()
    personnel = models.IntegerField()
    location = models.CharField(max_length=20)

class Reply(models.Model):
    comment = models.TextField() # TextField 활용
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE) #ForeignKey 활용, 부모 삭제시 자식데이터 삭제 - CASCADE 설정
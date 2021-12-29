from django.db import models
import uuid
import datetime
# Create your models here.
class Data(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=1000)
    email=models.EmailField(max_length=255)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    objects=models.Manager()
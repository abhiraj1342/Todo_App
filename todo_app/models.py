from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TodoList(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    task=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    
    def __str__(self):
        return self.task
from django.db import models
from django.contrib.auth.models import User
 
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    description = models.TextField()
 
    def __str__(self) -> str:
        return self.name
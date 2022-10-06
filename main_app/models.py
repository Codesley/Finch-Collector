from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Finch(models.Model):

    name = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    description = models.TextField(max_length=500)
    verified_finch = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
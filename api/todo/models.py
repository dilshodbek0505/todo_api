from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    auth = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 255)
    description = models.TextField()
    is_done = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    def __str__(self) -> str:
        return f"{self.name}  - {self.auth.username}"
    

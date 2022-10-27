from django.db import models
from django.contrib.auth.models import AbstractUser

# User = get_user_model()

class User(AbstractUser):
    pass

class Lead(models.Model):   
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
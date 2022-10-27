from django.db import models

class Lead(models.Model):   
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)

class Agent(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
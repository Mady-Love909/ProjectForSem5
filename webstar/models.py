from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=50)
    mobno = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name
    

class Feedback(models.Model):
    desc = models.TextField()
    date = models.DateField()


    

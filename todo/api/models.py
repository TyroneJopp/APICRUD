from django.db import models

# Create your models here.
class Task(models.Model):               #This class will take models from the models import this class
    title = models.CharField(max_length=200) #A variable title will contain the 
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


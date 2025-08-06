from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=35)
    description = models.TextField(max_length=350)
    deadline_date = models.DateField(null=True)


    def __str__(self):
        return self.title




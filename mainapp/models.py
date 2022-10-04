from tkinter import CASCADE
from django.db import models
from authapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=128, unique=True)
    link = models.CharField(max_length=256, unique=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

from datetime import datetime, timedelta
from django.utils import timezone

from django.db import models
from auth_.models import MyUser


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    due_date = models.DateTimeField(default=timezone.now()+timedelta(days=3))
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    priority = models.IntegerField(default=0)
from datetime import datetime, timedelta
from django.utils import timezone

from django.db import models
from auth_.models import MyUser


class TaskListManager(models.Manager):
    def created_by_user(self, user):
        return self.filter(created_by=user)


class TaskListBase(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BusinessTaskList(TaskListBase):
    objects = TaskListManager()

    class Meta:
        verbose_name = 'Business Task List'
        verbose_name_plural = 'Business Task Lists'


class PersonalTaskList(TaskListBase):
    objects = TaskListManager()

    class Meta:
        verbose_name = 'Personal Task List'
        verbose_name_plural = 'Personal Task Lists'


class TaskBase(models.Model):
    D = 1
    P = 2
    NS = 3
    STATUS = (
        (D, 'done'),
        (P, 'pending'),
        (NS, 'not started'),
    )
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now(), blank=True)
    status = models.CharField(max_length=200, choices=STATUS, default=3)

    objects = TaskListManager()


class BusinessTask(TaskBase):
    priority = models.IntegerField(default=0)
    due_date = models.DateTimeField(default=timezone.now() + timedelta(days=3))
    objects = TaskListManager()

    @classmethod
    def count(cls):
        return cls.objects.count()

    @property
    def string_is_done(self):
        if self.status.choices == 1:
            return 'done'
        return 'not done'


class PersonalTask(TaskBase):
    objects = TaskListManager()

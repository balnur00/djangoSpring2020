from datetime import datetime, timedelta

from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone

from django.db import models
from auth_.models import MyUser
# from main.signals import todo_created


class TaskListManager(models.Manager):
    def created_by_user(self, user):
        return self.filter(created_by=user)


class TaskListBase(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class BusinessTaskList(TaskListBase):
    image = models.ImageField(upload_to='todo', null=True, blank=True)
    objects = TaskListManager()

    class Meta:
        verbose_name = 'Business Task List'
        verbose_name_plural = 'Business Task Lists'


class PersonalTaskList(TaskListBase):
    objects = TaskListManager()

    class Meta:
        verbose_name = 'Personal Task List'
        verbose_name_plural = 'Personal Task Lists'


# @receiver(signals.pre_save, sender=PersonalTaskList)
# def create_pertl(sender, instance, created, **kwargs):
#     print("Personal tl created")


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
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    status = models.CharField(max_length=200, choices=STATUS, default=3)

    objects = TaskListManager()


class BusinessTask(TaskBase):
    priority = models.IntegerField(default=0)
    due_date = models.DateTimeField(default=datetime.now() + timedelta(days=3))
    task_list = models.ForeignKey(BusinessTaskList, on_delete=models.CASCADE)
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
    image = models.ImageField(upload_to='todo', null=True, blank=True)
    task_list = models.ForeignKey(PersonalTaskList, on_delete=models.CASCADE)
    objects = TaskListManager()


class ReceiverSignal(models.Model):
    desc = models.CharField(max_length=200)
    objects = models.Manager()


# signals.post_save.connect(receiver=todo_created, sender=BusinessTaskList)

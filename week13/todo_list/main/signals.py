from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import BusinessTaskList, Receiver


@receiver(post_save, sender=BusinessTaskList)
def todo_created(sender, instance, created, **kwargs):
    if created:
        rec = f'In the shop appears exclusive product: {instance.title}'
        Receiver.objects.create(desc=rec)
        print("customer created")

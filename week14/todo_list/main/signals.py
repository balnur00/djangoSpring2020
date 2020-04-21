from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import BusinessTaskList, ReceiverSignal


@receiver(post_save, sender=BusinessTaskList)
def todo_created(sender, instance, created, **kwargs):
    if created:
        rec = f'In the shop appears exclusive product: {instance.title}'
        r = ReceiverSignal(desc=rec)
        r.save()
        print("signal works")

# signals.post_save.connect(receiver=signals.todo_created, sender=BusinessTaskList)
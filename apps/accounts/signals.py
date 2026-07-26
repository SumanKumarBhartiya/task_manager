from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.notifications.models import Notification
from .models import User


@receiver(post_save, sender=User)
def create_welcome_notification(sender, instance, created, **kwargs):

    if created:
        Notification.objects.create(
            user=instance,
            message=f"Welcome {instance.username}"
        )
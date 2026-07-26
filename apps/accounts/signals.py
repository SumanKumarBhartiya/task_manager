from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.accounts.models import User
from apps.notifications.models import Notification


@receiver(post_save, sender=User)
def create_welcome_notification(sender, instance, created, **kwargs):

    if created:
        Notification.objects.create(
            user=instance,
            message=f"Welcome {instance.username}"
        )
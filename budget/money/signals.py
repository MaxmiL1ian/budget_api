from user.models import User
from money.models import Remain
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_generate_code(sender, instance, created, *args, **kwargs):
    if created:
        Remain.objects.create(user=instance)


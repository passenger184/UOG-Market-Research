from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Product


@receiver(pre_save, sender=Product)
def set_status(sender, instance, **kwargs):
    if instance.price is None or instance.availability is None:
        instance.status = 'pending'
    else:
        instance.status = 'responded'
   

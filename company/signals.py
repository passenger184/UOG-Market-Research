from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Companie

@receiver(post_save, sender=Companie)
def send_activation_email(sender, instance, **kwargs):
    mes = f'Dear {instance.user.username},\n\nThank you for registering with our website.\nWe are pleased to inform you that your account with {instance.companiesName.upper()} has been activated.\nYou can now log in to your account and start using it.\n\nhttp://127.0.0.1:8000/signin\n\nThank you again for joining our community, and we look forward to working with you.\n\nBest regards,\nUOG Market Research'

    if instance.active:
        user_email = instance.user.email
        subject = 'Account Activated'
        message = mes
        from_email = 'Hussenjebril12@gmail.com'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)



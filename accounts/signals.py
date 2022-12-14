from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account,Referral,LoginHistory
from appi import utils


@receiver(post_save, sender=Account)
def create_referral(sender, instance, created, **kwargs):
    if created:
        Referral.objects.create(user=instance)
        utils.send_regMail(instance.email)

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


User._meta.get_field('email')._unique = True


class AdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_additionalinfo(sender, instance, created, **kwargs):
    if created:
        AdditionalInfo.objects.create(user=instance)
    instance.additionalinfo.save()

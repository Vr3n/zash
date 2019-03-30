from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, CustomUser

# write signals here.

# For receiving signal from CustomUser model to save it in Profile model.
@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# For receiving signal from CustomUser model to saving it in Profile model.
@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

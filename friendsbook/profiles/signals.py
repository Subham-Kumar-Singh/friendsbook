from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# this user is always craeting a profile for a user if a new user is created
@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
        
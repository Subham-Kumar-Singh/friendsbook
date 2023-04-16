from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,RelationShip

# this user is always craeting a profile for a user if a new user is created
@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

@receiver(post_save,sender=RelationShip)
def post_save_add_friends(sender,instance,created,**kwargs):
    sender_=instance.sender
    receiver_=instance.receiver
    status_=instance.status
    if status_=="accepted":
        sender_.friends.add(receiver_.user)
        receiver_.friends.add(sender_.user)
        sender_.save()
        receiver_.save()
        
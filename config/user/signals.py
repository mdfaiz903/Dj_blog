
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import profileModel

# Define a signal
@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
            profileModel.objects.create(user=instance)

        # Perform some action when a new user is created
    # print("A new user has been created:", instance.username)
@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
      instance.userprofiledata.save()

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class profileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE ,related_name = 'userprofiledata')
    image = models.ImageField(upload_to='profile_img/',blank=True,null=True,default='av.jpg')

    def __str__(self):
        return f"{self.user.username}_profile"

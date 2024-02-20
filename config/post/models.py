from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class post_model(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class User(models.Model):
    pic=models.ImageField(upload_to="profile")

    def __str__(self):
        return str(self.pic)

from django.conf import settings
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    about_me = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Profile for {}".format(self.user.username)

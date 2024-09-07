from django.db import models
from django.conf import settings
import datetime

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<username>/year/month/day/<filename>
    return f'{instance.user.username}/{datetime.datetime.now().strftime("%Y/%m/%d")}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    date_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=user_directory_path, blank=True)

    def __str__(self):
        return self.user.username

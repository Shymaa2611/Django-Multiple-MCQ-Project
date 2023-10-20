from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractBaseUser, PermissionsMixin):
    objects = CustomUserManager()
    username=models.CharField(max_length=20)
    email = models.EmailField(unique=True) 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
class Chapter(models.Model):
    chapter=models.FileField(upload_to='chapters/',blank=True,null=True)
    final_degree=models.IntegerField(blank=True,null=True)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE,blank=True,null=True)
    std_degree=models.DecimalField(max_digits=5,decimal_places=3,blank=True,null=True)
    def __str__(self):
        return f"{self.user.email} Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


    

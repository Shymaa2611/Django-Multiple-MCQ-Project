from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Chapter(models.Model):
    chapter=models.FileField(upload_to='chapters/',blank=True,null=True)
    #answer=models.BooleanField(default=False)
class Question(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    question=models.CharField(max_length=100,blank=True,null=True)
    answer = models.CharField(max_length=100)


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE,blank=True,null=True)
    std_degree=models.IntegerField(blank=True,null=True)
    def __str__(self):
        return f"{self.user.email} Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s response to {self.question.content}"

    

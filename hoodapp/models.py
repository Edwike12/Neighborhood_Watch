from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    hood_logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)

#class profile
class Profile(models.Model):
    profile_photo=CloudinaryField('image')
    name=models.TextField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=50, blank=True, null=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)
    email=models.CharField(null=True, max_length=50)
    phone_number=models.IntegerField(null=True)

    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()

      def __str__(self):
        return f'{self.user.username} profile'

#class neighborhood
#class profile
#class  post
# class comments
#class business
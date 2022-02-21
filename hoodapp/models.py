from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Location(models.Model):
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name

class NeighborHood(models.Model):
    name = models.CharField(max_length=50)
    photo = CloudinaryField("image",null=True)
    content = models.TextField(max_length=600, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    occupants_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    health_cell = models.IntegerField(null=True, blank=True)
    police_hotline = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()
        
    def update_neighborhood(self):
        self.update()
    def update_occupants(self):
        self.update()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

#class profile
class Profile(models.Model):
    profile_photo=CloudinaryField('image')
    name=models.TextField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
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

class Post(models.Model):
    title = models.CharField(max_length=50,null=True)
    content = models.TextField(blank=True, null=True)
    photo = CloudinaryField("image",blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    
    class Meta:
        ordering = ['-pk']
        
    def __str__(self):
        return f'{self.title} Post'
    
    def delete_post(self):
        self.delete()
    

    def create_post(self):
        self.save()
        
    def update_post(self):
        self.update()

    
    
class Business(models.Model):
    photo = CloudinaryField("image",null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def find_business(cls, id):
        business = cls.objects.get(id=id)
        return business

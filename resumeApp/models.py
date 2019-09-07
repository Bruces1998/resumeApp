from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profiles' ,on_delete=models.CASCADE)
    # school = models.CharField(blank=True, null=True, max_length=100)
    image  = models.ImageField(upload_to='media/UserImages', default=None,null=True,blank=True)
    firstname = models.CharField(blank=True, null=True, max_length=100)
    lastname = models.CharField(blank=True, null=True, max_length=100)



    def __str__(self):
        return self.firstname
# class User(User,PermissionsMixin):
#     image  = models.ImageField(upload_to='media/UserImages', default=None,null=True,blank=True)
#     website = models.CharField(blank=True, null=True, max_length=100)
#     # email = models.EmailField()
#     def __str__(self):
#         return self.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



class Skill(models.Model):
    possed_by = models.ForeignKey(User,related_name='skills', on_delete=models.CASCADE,null=True)
    experience = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(blank=True,null=True,max_length=265)
    def __str__(self):
        return self.possed_by.username


class Work_Experience(models.Model):
    possed_by = models.ForeignKey(User, related_name='experiences', on_delete=models.CASCADE, null=True)
    name_of_org = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    bio = models.TextField()

    # def __str__(self):
    #     return self.possed_by.username

class Education(models.Model):
    possed_by = models.ForeignKey(User, related_name='educations', on_delete=models.CASCADE, null=True)
    name_of_institute = models.CharField(max_length=50, blank=True, null=True)
    course = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    # def __str__(self):
    #     return self.possed_by.username

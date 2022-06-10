from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    prefix = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    linkedin_user = models.URLField()
    company = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.username} ({self.user.id})'


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    type_of_code = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    turnover = models.IntegerField(default=0)
    employees = models.IntegerField(default=0)
    products = models.CharField(max_length=255)
    sectors = models.CharField(max_length=255)
    BOM_position = models.CharField(max_length=255)
    linkedin_company = models.URLField()
    email_company = models.EmailField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            CompanyProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.companyprofile.save()

    def __str__(self):
        return f'{self.address} ({self.user.id})'


'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # USER DATA
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    prefix = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    linkedin_user = models.URLField()
    company = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)

    type_of_code = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    turnover = models.IntegerField(default=0)
    employees = models.IntegerField(default=0)
    products = models.CharField(max_length=255)
    sectors = models.CharField(max_length=255)
    BOM_position = models.CharField(max_length=255)
    linkedin_company = models.URLField()
    email_company = models.EmailField()

    #  LEARN !!
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.username} ({self.user.id}) '''

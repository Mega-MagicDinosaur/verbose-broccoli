from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # USER DATA
    telephone_number = models.IntegerField(null=True)
    linkedin_profile = models.URLField()
    company = models.CharField(max_length=255)
    # select -> department =
    job_title = models.CharField(max_length=255)

    # COMPANY DATA
    # select type_code = (ateco, nace)
    code = models.IntegerField(null=True)
    company_address = models.CharField(max_length=255)
    # select turnover = 10MIL-20MIL .. 20MIL-30MIL ..
    # select employees = 1-10 .. 10-20 ..
    products = models.CharField(max_length=255)
    BOM_position = models.CharField(max_length=255)
    company_linkedin = models.URLField()
    company_email = models.EmailField()

    #  LEARN !!
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f'{self.user.username} ({self.user.id})'

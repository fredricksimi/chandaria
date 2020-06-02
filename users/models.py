from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .countries import COUNTRIES
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings
from PIL import Image
from django.dispatch import receiver

from .managers import CustomUserManager


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    username = None
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    nationality = models.CharField(choices=COUNTRIES, max_length=150)
    country_of_residence = models.CharField(choices=COUNTRIES, max_length=150)
    date_of_birth = models.DateField(null=True)
    sex = models.CharField(choices=GENDER, max_length=200)
    photo = models.ImageField(upload_to='profile_pics/%Y/%m/%d', default='default.jpg', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.template.defaultfilters import slugify

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from customuser.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        
        string_slug = self.first_name + '-' + str(self.date_joined.strftime('-%d-%m-%M'))
        self.slug = slugify(string_slug)

        super(CustomUser, self).save(*args, **kwargs)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

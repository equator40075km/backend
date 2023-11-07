from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from articles.models import Article


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=170, blank=True)
    bday = models.DateField(default=None, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True)
    is_author = models.BooleanField(default=False)
    favorites = models.ManyToManyField(Article, blank=True, related_name='+')
    avatar = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

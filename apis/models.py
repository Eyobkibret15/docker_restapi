from django.db import models


# Create your models here.


class country(models.Model):
    country = models.TextField()

    def __str__(self):
        return self.country


class city(models.Model):
    city = models.TextField()
    level = models.TextField()
    country = models.ForeignKey(country, related_name="citys", on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class hotel(models.Model):
    hotel = models.TextField()
    price = models.TextField()
    city = models.OneToOneField(city, related_name="hotels", on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel


# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

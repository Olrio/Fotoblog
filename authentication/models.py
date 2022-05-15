from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )


    profile_photo = models.ImageField(verbose_name='Photo de profil', upload_to='media/bird-9950_1920.jpg')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

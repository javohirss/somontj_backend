from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(models.Model):
    ROLE_CHOICES = [
        ('U', 'USER'),
        ('M', 'MODERATOR'),
        ('A', 'ADMIN'),
        ('SA', 'SUPERADMIN'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    has_whatsapp = models.BooleanField(default=False)
    email = models.EmailField(max_length=255, unique=False)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



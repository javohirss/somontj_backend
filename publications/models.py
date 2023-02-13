from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField(null=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)

    def save(self, checkParent=True, *args, **kwargs):
        super(Category, self).save()
        if self.parent and checkParent:
            self.parent.parent = self
            self.parent.save(checkParent=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    CONDITION_CHOICES = [
        ('BAD', 'BAD'),
        ('GOOD', 'GOOD'),
    ]

    name = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=True)
    condition = models.CharField(max_length=255, choices=CONDITION_CHOICES)
    link_to_video = models.URLField(max_length=1000, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




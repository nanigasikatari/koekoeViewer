from django.conf import settings
from django.db import models


class Address(models.Model):
    url = models.CharField(max_length=100)
    contributor = models.CharField(max_length=100, blank=True)
    number=models.CharField(max_length=10)
    title = models.CharField(max_length=100, blank=True)
    comment = models.TextField(blank=True)
    star=models.BigIntegerField()

    def starshine1(self):
        self.star=1
        self.save()

    def starshine2(self):
        self.star=2
        self.save()

    def starshine3(self):
        self.star=3
        self.save()

    def __str__(self):
        return self.title

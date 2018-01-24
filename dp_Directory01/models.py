# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class dr01fs01_inpt1(models.Model):
    dr01FI01_IV = models.IntegerField()
    dr01FI02_CV = models.CharField(max_length=250)
    dr01FI03_EV = models.EmailField(max_length=250)
    dr01FI04_IPV = models.IPAddressField
    dr01FI05_DT = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.dr01FI01_IV


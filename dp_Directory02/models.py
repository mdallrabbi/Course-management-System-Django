# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm


# Create your models here.

class dr02fs01_inpS1(models.Model):
    dr02fs01_Char1 = models.CharField(max_length=250)
    dr02fs01_Char2 = models.CharField(max_length=250)
    dr02fs01_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.dr02fs01_Char1


class dr02fs01_inptS2(models.Model):
    dr02fs01_Char3 = models.CharField(max_length=250)
    dr02fs01_FChar1 = models.ManyToManyField(dr02fs01_inpS1)

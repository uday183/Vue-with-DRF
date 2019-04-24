# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    edition = models.CharField(max_length=20)

    def __str__(self):
        return "%s----%s" %(self.title, self.author)
        


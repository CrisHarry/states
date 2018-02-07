# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class countries(models.Model):

    countries_code = models.CharField(max_length=20)
    countries_name = models.CharField(max_length=20)

class states(models.Model):
        state_name = models.CharField(max_length=20)
        foreign = models.ForeignKey(countries, on_delete=models.CASCADE)

        def __func__(self):
            return self.countries.countries_name
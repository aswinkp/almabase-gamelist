# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Table8(models.Model):
    title = models.CharField(max_length=56, primary_key=True)
    platform = models.CharField(max_length=16, blank=True, null=True)
    score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    genre = models.CharField(max_length=17, blank=True, null=True)
    editors_choice = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TABLE 8'

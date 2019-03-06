from django.db import models

from ford3.models.campus import Campus

class CampusEvent(models.Model):
  id = models.IntegerField(
    blank=False,
    null=False,
    unique=True,
    help_text='Key of qualification',
    primary_key=True)
  campus_id = models.ForeignKey(
      Campus,
      on_delete=models.CASCADE)
  name = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)
  date_start = models.DateField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  date_end = models.DateField(
    blank=False,
    null=False,
    unique=False,
    help_text='')
  http_link = models.CharField(
    blank=False,
    null=False,
    unique=False,
    help_text='',
    max_length=255)
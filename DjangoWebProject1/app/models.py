"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Event(models.Model):
    """A poll object for use in the application views and repository."""
    start_date = models.DateField('start_date')
    start_time = models.TimeField()
    start_datetime = models.DateTimeField()
    start_month = models.IntegerField()
    start_year = models.IntegerField()

class Question(models.Model):
    question_text = models.TextField()
    pub_date = models.DateTimeField()
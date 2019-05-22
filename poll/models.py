from django.db import models

# Create your models here.
class Choice(models.Model):

    choice_name = models.CharField(max_length=255)
    choice_created = models.DateTimeField(auto_now=True)


class Poll(models.Model):

    poll_question = models.CharField(max_length=255)
    poll_creator = models.CharField(max_length=255)
    poll_created = models.DateTimeField(auto_now=True)

    poll_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
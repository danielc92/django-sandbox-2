from django.db import models

# Create your models here.
class Poll(models.Model):

    poll_question = models.CharField(max_length=255)
    poll_creator = models.CharField(max_length=255)
    poll_created = models.DateTimeField(auto_now=True)

class Choice(models.Model):

    choice_name = models.CharField(max_length=255)
    choice_created = models.DateTimeField(auto_now=True)
    poll_question = models.ForeignKey(Poll, 
                                      on_delete=models.CASCADE)
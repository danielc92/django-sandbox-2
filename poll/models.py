from django.db import models

# Create your models here.
class Poll(models.Model):

    poll_question = models.CharField(max_length=255)
    poll_creator = models.CharField(max_length=255)
    poll_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.poll_question

class Choice(models.Model):

    choice_name = models.CharField(max_length=255)
    choice_created = models.DateTimeField(auto_now=True)
    poll_question = models.ForeignKey(Poll, 
                                      on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_name
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

class Suburb(models.Model):
    suburb_name=CharField(max_length=40)


class Employment(models.Model):

    EMPLOYED = 'EMP'
    UNEMPLOYED = 'UNE'
    RETIRED = 'RET'
    STUDENT = 'STU'

    EMP_CHOICES = [
        (EMPLOYED, 'Currently Employed'),
        (UNEMPLOYED, 'Currently Unemployed'),
        (RETIRED, 'Retired from working'),
        (STUDENT, 'I am a student')
    ]


    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    emp_status = models.CharField(choices=EMP_CHOICES, max_length=3, default=STUDENT)
    age = models.DateField()
    suburb = models.ManyToManyField(Suburb)


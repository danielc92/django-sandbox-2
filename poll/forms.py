from django import forms
from django.contrib.admin import widgets
from .models import Choice, Poll, Employment

forms.DateInput.input_type="date"


class EmpForm(forms.ModelForm):

    class Meta:
        model = Employment
        fields = ['first', 'last', 'emp_status', 'age', 'fav_question']

    

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_name', 
                  'poll_question']

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['poll_question',
                  'poll_creator']



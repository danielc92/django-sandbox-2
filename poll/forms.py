from django import forms

from .models import Choice, Poll


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



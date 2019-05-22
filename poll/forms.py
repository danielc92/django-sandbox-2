from django import forms

from .models import Choice, Poll


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_name', 
                  'choice_created']

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['poll_question',
                  'poll_creator',
                  'poll_created',
                  'poll_choice']
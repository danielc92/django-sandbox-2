from django import forms
from django.contrib.admin import widgets
from .models import Choice, Poll, Employment, Suburb


forms.DateInput.input_type="date"

class EmpForm(forms.ModelForm):
    
    class Meta:
        model = Employment
        fields = ['first', 'last', 'emp_status', 'age', 'suburb']

    def __init__(self, *args, **kwargs):

        super(EmpForm, self).__init__(*args, **kwargs)

        self.fields['suburb'].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields['suburb'].queryset = Suburb.objects.all()

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



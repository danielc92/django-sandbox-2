from django.shortcuts import render
from django.http import HttpResponse
from .forms import PollForm, ChoiceForm, EmpForm


# Create your views here.
def bulmafy(form):
    form = form.as_p()
    form = form.replace('<label', '<label class="label"')
    form = form.replace('<input', '<input class="input"')

    return form

from .models import Poll, Choice

def make_poll(request):

    if request.method == 'POST':

        form = PollForm(request.POST)

        if form.is_valid():
            # First create the Poll
            poll = Poll(**form.cleaned_data)
            poll.save()
            print('Poll has been saved')

            for choice_id in ['choice-1', 'choice-2', 'choice-3', 'choice-4']:
                content = request.POST.get(choice_id)
                content = content.strip()
                if len(content) > 0 and len(content) < 100:
                    choice = Choice(choice_name=content, poll_question=poll)
                    choice.save()
                    print('Choice has been saved')

            return HttpResponse('Success')

        else:
            errors = form.errors
            print(errors)
            return HttpResponse('Error')

    else:

        form = PollForm()

    context = {'form' : bulmafy(form)}

    return render(request, 'make_poll.html', context)


def make_emp(request):

    if request.method == 'POST':

        form = EmpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Success')

        else:
            errors = form.errors
            print(errors)
            return HttpResponse('Error')

    else:

        form = EmpForm()
        print(form)

    context = {'form' : form}

    return render(request, 'make_emp.html', context)

def make_emp_manual(request):

    if request.method == 'POST':

        form = EmpForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Success')

        else:
            errors = form.errors
            print(errors)
            return HttpResponse('Error')

    else:

        form = EmpForm()
        print(form)

    context = {'form' : form}

    return render(request, 'manual-form.html', context)
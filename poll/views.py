from django.shortcuts import render
from django.http import HttpResponse
from .forms import PollForm, ChoiceForm
# Create your views here.

def make_poll(request):

    if request.method == 'POST':

        form = PollForm(request.POST)

        if form.is_valid():
            print('form is valid')
            return HttpResponse('Success')

    else:

        form = PollForm()

    context = {'form' : form}

    return render(request, 'make_poll.html', context)
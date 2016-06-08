from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import NameForm
from .models import kalat
from django import forms


def test(request):
    latest_question_list = kalat.objects.order_by('id')[:2]
    template = loader.get_template('result.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
        kala = kalat()
        kala.paikka = request.POST.get('paikka')
        kala.saaja = request.POST.get('saaja')
        kala.viehe = request.POST.get('viehe')
        kala.paino = request.POST.get('paino')
        kala.pituus = request.POST.get('pituus')
        kala.save()
    
    
    
    
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        return HttpResponse("Thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'form.html', {'form': form})
	
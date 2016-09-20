from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SaalisForm
from .forms import LoginForm
from .models import kalat
from django import forms 

def httpResponse(request):
    
    user = User.objects.create(username='testuser',password='!')
    user.set_password('pass')
    user.save()
    

    return HttpResponse("testuser created with password pass")

def login(request):
    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username,password=password)
            
            
            if user is not None:
                if user.is_active:
                    auth_login(request,user)
                    return HttpResponse("You've been logged in")
        return HttpResponse("Failed to login")
                     
        
    else:
        form = LoginForm()
        return render(request, 'loginform.html', {'form': form})
        

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
        form = SaalisForm(request.POST, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False) 
            instance.save()
        """
		# create a form instance and populate it with data from the request:
        form = SaalisForm(request.POST)
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
		"""
        return HttpResponse("Thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SaalisForm()

    return render(request, 'form.html', {'form': form})
	
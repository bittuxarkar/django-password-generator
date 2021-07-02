from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'vhjgf765'})

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
            characters.extend(list('!@#$%^&*()_+?/'))

    if request.GET.get('numbers'):
            characters.extend(list('1234567890'))
    
    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

    length = int(request.GET.get('length',15))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
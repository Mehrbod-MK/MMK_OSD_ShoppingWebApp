from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def login(request):
    return render(request, 'registration/login.html')

def userAuth(request):
    user_Username = request.POST["user_Username"]
    user_Password = request.POST["user_Password"]

    user = authenticate(request=request, username=user_Username, password=user_Password)
    if(user is not None):
        return HttpResponse('OK!')
    else:
        return HttpResponse('No such user!')

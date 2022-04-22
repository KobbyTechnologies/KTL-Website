from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(request, 'index.html')

def navbar(request):
    return render(request, 'navbar.html')

def footer(request):
    return render(request, 'footer.html')

def contactus(request):
    return render(request, 'contactus.html')
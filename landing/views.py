from django.shortcuts import render

# Create your views here.


def landing(request):
    
    
    
    return render(request, 'index.html')

def about_us(request):
    today = "Tuesday"
    ctx= {"leo":today}
    return render(request,"about.html")
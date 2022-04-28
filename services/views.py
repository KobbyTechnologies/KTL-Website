from django.shortcuts import render

# Create your views here.
def service_request(request):
    
    return render(request,"service.html")
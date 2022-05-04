from django.shortcuts import render

# Create your views here.
def service_request(request):
    return render(request, 'service.html')

def single_request(request):
    return render(request, 'servicedetails.html')       

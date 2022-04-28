from django.shortcuts import render

# Create your views here.
def service_request(request):
    return render(request, 'services.html')

def single_request(request):
    return render(request, 'singleservice.html')       

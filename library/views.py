from django.shortcuts import render

# Create your views here.
def  stories_view(request):
    return render(request, 'success-stories.html')
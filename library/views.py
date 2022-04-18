from django.shortcuts import render

# Create your views here.
def  stories_view(request):
    return render(request, 'success-stories.html')


def  story_detail(request):
    return render(request, 'story.html')


def events(request):
    return render(request, 'events.html')


def csr_view(request):
    return render(request, 'csr.html')
    
    
def csr_detail_view(request):
    return render(request, 'csr-detail.html')

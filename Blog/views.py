from django.shortcuts import render

# Create your views here.
def Blog_request(request):
    return render(request, 'Blog.html')
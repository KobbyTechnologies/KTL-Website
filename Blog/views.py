from django.shortcuts import render

# Create your views here.
def blog_request(request):
    return render(request, 'Blog.html')

def blog_detail_request(request):
    return render(request, 'blog-details.html')    
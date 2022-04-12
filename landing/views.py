from django.shortcuts import render

# Create your views here.


def landing(request):
    return render(request, 'index.html')
    
def solution(request):
    return render(request, 'solution.html')


def solution_view(request):
    return render(request, 'single_solution.html')



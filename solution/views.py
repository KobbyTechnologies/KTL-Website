from django.shortcuts import render

# Create your views here.
def solution(request):
    return render(request, 'solution.html')


def solution_view(request):
    return render(request, 'single-solution.html')
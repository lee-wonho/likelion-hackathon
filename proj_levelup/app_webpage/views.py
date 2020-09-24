from django.shortcuts import render

# Create your views here.

def ex_pr(request):
    return render(request, 'ex_pr.html')
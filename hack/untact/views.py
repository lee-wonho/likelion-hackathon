from django.shortcuts import render,redirect
from .models import Genre, Info

# Create your views here.

def home(request):
    genre_obj = Genre.objects.all()

    context={
        'genre_obj_list': genre_obj
    }

    return render(request, 'index.html', context)

def show(request, genre_pk):
    info_obj = Info.objects.all()

    context = {
        'info_obj': info_obj,
        'genre_pk': genre_pk
    }

    if request.method=='POST':
        return redirect('home')

    return render(request, 'show.html',context)
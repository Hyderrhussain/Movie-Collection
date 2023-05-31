from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import movieform
from .models import movie

def index(request):
    print(request.GET)
    return render(request, "home.html")

def movies(request):
    if request.method == "POST":
        form = movieform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = movieform()
    return render(request,'index.html',{'form':form})

def show(request):
    Movie = movie.objects.all()
    return render(request,"show.html",{'movie':Movie})

def edit(request, id):
    editmovie = movie.objects.get(id=id)
    return render(request,'edit.html',{'movie':editmovie})

def update(request, id):
    editmovie = movie.objects.get(id=id)
    form = movieform(request.POST, instance =editmovie)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'movie': editmovie})

def destroy(request, id):
    editmovie = movie.objects.get(id=id)
    editmovie.delete()
    return redirect("/show")
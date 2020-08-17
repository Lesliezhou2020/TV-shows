from django.shortcuts import redirect, render
from TVApp.models import *

def index(request):
    return redirect('/shows')


def shows(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new(request):
    return render(request, 'new.html')

def detail(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'detail.html', context)

def edit(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit.html', context)
    

def add_show(request):
    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc'],
    )
    return redirect('/shows/{}'.format(show.id))

def update_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['desc']
    show.save()
    return redirect('/shows/{}'.format(show.id))

def delete(request, show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')



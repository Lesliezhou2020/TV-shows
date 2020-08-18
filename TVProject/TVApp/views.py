from django.shortcuts import redirect, render
from django.contrib import messages
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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
        
    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        desc = request.POST['desc'],
    )
    return redirect('/shows/{}'.format(show.id))

def update_show(request, show_id):
    errors = Show.objects.update_validator(request.POST, show_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/{}/edit'.format(show_id))

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



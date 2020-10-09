
from django.shortcuts import render, HttpResponse, redirect
from .models import*

def index(request):
    context = {
        'dojos' : Dojo.objects.all(),
        'ninjas' : Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    print(request.POST)
    #save the dojo to the db
    newly_added_dojo=Dojo.objects.create(
        name = request.POST['name'],
    #first name is from model.py
    #second name is from html name='name'
        city = request.POST['city'],
        state = request.POST['state'],
    )
    print('Create: ', newly_added_dojo)
    return redirect('/')


def add_ninja(request):
    print(request.POST)

    dojo_from_db = Dojo.objects.get(id=request.POST['dojo'])
    #'dojo' is from html <selected name='dojo'>

    newly_added_ninja = Ninja.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            dojo = dojo_from_db,
        )
    print('Create: ', newly_added_ninja)
    return redirect('/')

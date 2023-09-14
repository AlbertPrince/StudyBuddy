from django.shortcuts import render
from django.http import HttpResponse, Http404

rooms = [
    {'id' : 1, 'name': 'lets learn python'},
    {'id' : 2, 'name': 'lets learn java'},
    {'id' : 3, 'name': 'lets learn C++'}
]

# Create your views here.
def home(request):
    context = {"rooms": rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for item in rooms:
        if item['id'] == pk:
            room = item
        context = {'room': room}
    return render(request, 'base/room.html', context)

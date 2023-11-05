from django.shortcuts import render



rooms = [{"id":1, "name":"Edris"},
          {"id":2, "name":"Hamed"},
          {"id":3, "name":"Nawid"}]

def home(request):
    return render(request, 'Base/home.html', {"rooms":rooms})

def room(request):
    return render(request, 'Base/room.html')
# chat/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from members.models import Member


@login_required
def room(request, room_name):
    user = request.user
    k = Member.objects.filter(username=user).get()
    cluster = k.cluster
    return render(request, "chat/room.html", context={"cluster":cluster, "user":user})

@login_required
def room_number_guess(request):
    user = request.user
    k = Member.objects.filter(username=user).get()
    cluster = k.cluster
    return room(request, cluster)

@login_required
def index(request):
    user = request.user
    k = Member.objects.filter(username=user).get()
    cluster = k.cluster
    return render(request, template_name="chat/index.html", context={"cluster":cluster, "user":str(user.username)})
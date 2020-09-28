from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from .models import Computation
# New Below
from datetime import datetime

def home(request):
    if request.method == 'POST':
        return new_calc(request)
    computations = Computation.objects.all()
    # {'computations':computations} included for possible extentions later
    return render(request, 'user.html', {'computations':computations})


def new_calc(request):
    if request.method == 'POST':
        compl = request.POST.get('comp')
        user = User.objects.first()
        t = datetime.now()
        s = t.strftime("%c %Z")
        Computation.objects.create(comp = compl, entered_at = s)
    return HttpResponse('')


def find_objects(request):
    count = Computation.objects.count()
    # Display up to 10 most recent via websockets (channels)
    if count < 10:
        computations = Computation.objects.order_by("-entered_at")[:count]
    else:
        computations = Computation.objects.order_by("-entered_at")[:10]
    data = serializers.serialize("json", computations)
    response = JsonResponse({'data': data})
    return response

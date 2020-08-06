from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core import serializers

# from django.http import HttpResponse
from django.shortcuts import render
from .models import Computation

def home(request):
    '''# db objects to access (see models.py)
    computations = Computation.objects.all()
    
    # old below
    #return render(request, 'user.html')
    
    return render(request, 'user.html', {'computations':computations})'''
    if request.method == 'POST':
        return new_calc(request)
    # return render(request, 'user.html')
    computations = Computation.objects.all()
    return render(request, 'user.html', {'computations':computations})


def new_calc(request):
    # calculation = get_object_or_404(Calculation, pk=pk)
    print("Before Testing")
    if request.method == 'POST':
        print("Testing")
    
        compl = request.POST.get('comp')
        
        user = User.objects.first()  # TODO: get the currently logged in user
        
        Computation.objects.create(
            comp = compl,
        )
        #calculation.save()
    
        #computations = Computation.objects.all()
        #return HttpResponse('OK')
    
        '''user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)

        return render(request, 'new_topic.html', {'board': board})
        # db objects to access (see models.py)
        # computations = Computation.objects.all()
    
        # old below
        #return render(request, 'user.html')'''
        #return render(request, 'user.html', {'computations':computations})
    #return {"value1":"value","value2":"value"}
    return HttpResponse('')


def find_objects(request):
    computations = Computation.objects.all()
    computations = Computation.objects.order_by("-entered_at")[:10]
    data = serializers.serialize("json", computations)
    response = JsonResponse({'data': data})
    return response

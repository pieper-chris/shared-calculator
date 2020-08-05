from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.contrib.auth.models import User

# from django.http import HttpResponse
from django.shortcuts import render
from .models import Computation

def home(request):
    '''# db objects to access (see models.py)
    computations = Computation.objects.all()
    
    # old below
    #return render(request, 'user.html')
    
    return render(request, 'user.html', {'computations':computations})'''
    return render(request, 'user.html')


def new_calc(request, pk):
    # calculation = get_object_or_404(Calculation, pk=pk)
    
    if request.method == 'POST':
    
        comp = request.POST['computation']
        
        user = User.objects.first()  # TODO: get the currently logged in user
        
        calculation = Computation.objects.create(
            comp = comp,
            created_by = user
        )

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

    return render(request, 'new_topic.html', {'board': board})'''
    # db objects to access (see models.py)
    computations = Computation.objects.all()
    
    # old below
    #return render(request, 'user.html')
    
    return render(request, 'user.html', {'computations':computations})

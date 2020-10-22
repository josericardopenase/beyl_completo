from django.shortcuts import render
from .models import Plan

# Create your views here.
def home(request):


    return render(request, 'pages/home.html')



def plans(request, plan = ""):

    context = {
        'plans' : Plan.objects.all().prefetch_related('features'),
        'plan' : plan
    }

    return render(request, 'pages/plans.html', context)

def team(request):
    
    context = {
        'none' : 'none'
    }

    return render(request, 'pages/team.html', context)
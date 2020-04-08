from django.shortcuts import render
from .models import Agents
# Create your views here.


def agents_list(request):
    agents_list = Agents.objects.all()
    template = 'agents/agents.html'
    context = {
        'agents_list' : agents_list
    }

    return render(request, template, context)
from django.shortcuts import render
from property.models import Property , Category
from agents.models import Agents
from .models import Services
from django.db.models import Count



# Create your views here.
def home(request):
    services_list = Services.objects.all()[:6]
    category_list_home = Category.objects.annotate(
        property_count=Count('property')
        ).values(
            'category_name',
            'property_count',
            'image'
            )[:4]
    print(category_list_home)
    property_list_home = Property.objects.all()
    agent_list_home = Agents.objects.all()[:4]
    template = 'home/home.html'
    context = {
        'category_list_home' : category_list_home , 
        'property_list_home' : property_list_home ,
        'agent_list_home' : agent_list_home ,
        'services_list' : services_list

    }

    return render(request , template, context)
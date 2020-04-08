from django.shortcuts import render
from .models import Property, Category
from .forms import ReserveForm
from django.db.models import Q
# Create your views here.



def property_list(request):
    property_list = Property.objects.all()
    category_list_again = Category.objects.all()[:4]
    template = 'property/list.html'

    address_query = request.GET.get('q')
    p_type_query = request.GET.get('p_type')
    if address_query and p_type_query :
        property_list = property_list.filter(
            Q(name__icontains = address_query) &
            Q(property_type__icontains = p_type_query)
        ).distinct()

    context = {
        'property_list' : property_list ,
        'category_list_again' : category_list_again
    }

    return render(request , template , context)

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReserveForm()

    context = {
        'property_detail' : property_detail , 
        'reserve_form' : reserve_form
    }

    return render(request , template , context)

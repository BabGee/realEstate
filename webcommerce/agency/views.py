from django.shortcuts import render
from property.models import Property



def home(request):
    context = {
        'all_property' : Property.objects.all(),
    }
    return render(request, 'agency/index.html', context)

def about(request):
    context = {
        'all_property' : Property.objects.all(),
    }
    return render(request, 'agency/about.html', context)

def pproperty(request, pk):
    stat = Property.objects.get(pk=pk).status
    context = {
        'property' : Property.objects.get(pk=pk), 
        'status' : Property.objects.filter(status=stat),  
    }
    return render(request, 'agency/property_detail.html', context)        

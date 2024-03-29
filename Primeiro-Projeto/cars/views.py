from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cars_view(request):
    return render(
        request, 
        'pages/cars.html', 
        {'cars': {'model': 'Astra 2.0'} }
    )
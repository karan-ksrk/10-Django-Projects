from django.shortcuts import render
from .models import Dish

def home(request):
    dishes = Dish.objects.all()
    context = {"dishes": dishes}
    return render(request, 'Menu/Home.html', context)
from django.shortcuts import render
from .models import *
def home(request):
    return render(request, 'Home/index.html')

def resume(request):
    resume = Resume.objects.first()

    context = {'resume':resume}
    return render(request, 'Home/resume.html', context)

def work(request):
    return render(request, 'Home/works.html')

def contact(request):
    return render(request, 'Home/contacts.html')
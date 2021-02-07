from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        data = {"message_name": message_name, "message_email": message_email}

        # Send Email
        send_mail(
         message_name, # subject
         message, # message
         message_email, # from email
         ['bigbang0047@gmail.com'],  # to email
         fail_silently=False,  
        )

        return render(request, 'contact.html', data)
    
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def pricing(request):
    return render(request, 'pricing.html', {})
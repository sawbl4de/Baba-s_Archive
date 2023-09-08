from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact, Poem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import login, authenticate

def index(request):
    # Your index view code here
    return render(request, "index.html")

def about(request):
    # Your about view code here
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent, we will get back to you soon!")

    return render(request, "contact.html")

def poems(request):
    # Your poems view code here
    list_title = Poem.objects.all()
    print(list_title)
    return render(request, "poems.html", {'list_title':list_title})

def articles(request):
    # Your articles view code here
    return render(request, "articles.html")

def stories(request):
    # Your stories view code here
    return render(request, "stories.html")

def poem_list(request):
    poems = Poem.objects.all()
    return render(request, 'poems.html', {'poems': poems})

def newsletter(request):
    # Your articles view code here
    return render(request, "newsletter.html")

def login(request):
    return render(request, 'newsletter.html')

@login_required
def home(request):
    return render(request, 'index.html')











from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact, Poem
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def about(request):
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
    list_title = Poem.objects.all()
    print(list_title)
    return render(request, "poems.html", {'list_title':list_title})

def articles(request):
    return render(request, "articles.html")

# def newsletter(request):
#     # Your articles view code here
#     return render(request, "newsletter.html")

def stories(request):
    return render(request, "stories.html")

@login_required
def home(request):
    return render(request, 'index.html')

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.success(request, 'Username must be under 10 characters!')
            return redirect('/writings/poems')
        if len(pass1) < 8:
            messages.success(request, 'Password must be atleast 8 characters long!')
            return redirect('/writings/poems')
        if pass1 != pass2:
            messages.success(request, 'Passwords do not match!')
            return redirect('/writings/poems')
        if not username.isalnum():
            messages.success(request, 'Username must contain only letters and numbers!')
            return redirect('/writings/poems')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, 'Your Account was created successfully! Login now')
        return redirect('/writings/poems')

    else:
        return HttpResponse("404 - Not found")
    

def handleLogin(request):
    if request.method=="POST": 
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in succesfully!')
            return redirect('/writings/poems')
        else:
            messages.success(request, 'Invalid credentials. Please try again.')
            return redirect('/writings/poems')

    # return HttpResponse('404 - Not Found')


def handleLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')

    return redirect('/writings/poems')

    










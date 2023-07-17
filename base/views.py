from django.shortcuts import render, get_object_or_404, redirect
from .models import Post , Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,"base/index.html", context)

def about(request):
    return render(request,"base/about.html")

def contact(request):
    return render(request, "base/contact.html")

def post(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    context = {"post":post}
    return render(request, "base/post.html",context)

def signin(request):
    if (request.method == "POST"):
        username = request.POST.get("uusernames")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=user)
        except:
            return messages.error(request,"log in details not correct")
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(user)
            return redirect("home.html") 
        else:
            messages.error(request,"log in details not correct");

    return render(request, "base/login.html")

def signup(request):
    if (request.method == "POST"):
        username = request.POST.get("uusernames")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=user)
        except:
            return messages.error(request,"log in details not correct")
        
        user = authenticate(request, username=username, password=password)

        if user:
            login(user)
            return redirect("home.html") 
        else:
            messages.error(request,"log in details not correct");

    return render(request, "base/signup.html")

def custom_404_page(request,exception):
    return render(request, '404.html', status=404)
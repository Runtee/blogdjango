from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"base/index.html")

def about(request):
    return render(request,"base/about.html")

def contact(request):
    return render(request, "base/contact.html")

def post(request, pk):
    return render(request, "base/post.html")
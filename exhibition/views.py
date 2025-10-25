from django.shortcuts import render

def home(request):
    return render(request, 'exhibition/home.html')

def about(request):
    return render(request, 'exhibition/about.html')

def gallery(request):
    return render(request, 'exhibition/gallery.html')

def contact(request):
    return render(request, 'exhibition/contact.html')

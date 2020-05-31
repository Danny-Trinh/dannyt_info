from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html', {'title': 'Welcome!'})


def forums(request):
    return render(request, 'portfolio/forums.html', {'title': 'Forums'})

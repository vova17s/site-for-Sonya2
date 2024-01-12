from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def allab(request):
    return render(request, "all.html")

def portfolio(request):
    return render(request, "portfolio.html")

def ticket(request):
    return render(request, "ticket.html")
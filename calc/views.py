
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html", {"name": "Shekhar"})


def add(request):
    value1 = int(request.POST["n1"])
    value2 = int(request.POST["n2"])
    res = value1 + value2
    return render(request, "result.html", {"result": res})

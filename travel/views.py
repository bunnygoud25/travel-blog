from django.shortcuts import render
from.models import Destination

def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def charminar(request):
    return render(request,'charminar.html')
def sarlarjung(request):
    return render(request,'sarlarjung.html')
def tankbund(request):
    return render(request,'tankbund.html')
def golkonda(request):
    return render(request,'golkonda.html')
def sanjeevaiah(request):
    return render(request,'sanjeevaiahpark.html')
def about(request):
    return render(request,'about.html')
def fav(request):
    return render(request,'about.html')

def empty(request):
    return render(request,'about.html')

from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        name = str(request.POST.get('Cmpname'))
        col = str(request.POST.get('Colname'))
        slogan=str(request.POST.get('Cmpslogan'))
        slog=str(request.POST.get('slog'))
        
        return render(request,'result.html',{'name':name,'col':col,'slogan':slogan,'slog':slog})

    else:
        return render(request,'index.html')
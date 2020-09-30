from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requset):
    return render(requset, 'index02.html')

def div(request):
    return render(request, 'div.html')
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def keuangan(request):
    return render(request, 'keuangan.html')
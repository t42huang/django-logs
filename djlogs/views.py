from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for djlogs"""
    return render(request, 'djlogs/index.html')
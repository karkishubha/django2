from django.shortcuts import render
def home(request):
    return render(request, 'friendapp.html')
# Create your views here.

from django.shortcuts import render
def home(request):
    return render(request, 'chatapp/home.html')
# Create your views here.

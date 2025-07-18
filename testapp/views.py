from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    current_dt= datetime.datetime.now()
    return render(request, 'test/home.html',{'dt':current_dt})
def about(request):
    info={'name':"Shubha",'address':"balkot",'number':986623632}
    return render(request, 'test/about.html',{'my_info':info})
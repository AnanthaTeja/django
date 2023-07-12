from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(s):
    return HttpResponse("Good Evening")
def demo(request,y):
    return HttpResponse(f"Good Evening {y}")
def st_det(request,sn,rol,ag):
    return HttpResponse(f"Student Details are: ,<a href='http://127.0.0.1:8000/s/'>ID</a> <br> Student Name: {sn}<br> Student Roll Num : {rol}<br> Student Age: {ag}<br>")
def frst(s):
    return render(s,"firstapp/demo.html")
def dsply(request,jk,a):
    return render(request,'firstapp/first.html',{'nm':jk,'ag':a})
def stud(request):
    return render(request,"firstapp/stform.html")
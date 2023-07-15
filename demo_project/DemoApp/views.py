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

def studG(request):
    print( f"Roll number : {request.GET}")
    return render(request,"firstapp/stform.html")

def studP(request):
    print(request.POST)
    if request.method=="POST":
        a=request.POST['rn']
        b=request.POST['stn']
        c=request.POST['age']
        d=request.POST['eml']
        e=request.POST['Gen']
        #print( f"Roll number : {request.POST}")
        return render(request,'firstapp/display.html',{'roll':a,"sname":b,"age":c,"mail":d,'Gen':e})
    return render(request,"firstapp/sformpost.html")
def boot(self):
    return render(self,'firstapp/bt.html')
def regform(self):
    return render(self,"firstapp/regiform.html")
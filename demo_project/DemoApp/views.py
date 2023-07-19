from django.shortcuts import render, redirect
from django.http import HttpResponse
from DemoApp.models import Student


# Create your views here.
def sample(s):
    return HttpResponse("Good Evening")


def demo(request, y):
    return HttpResponse(f"Good Evening {y}")


def st_det(request, sn, rol, ag):
    return HttpResponse(
        f"Student Details are: ,<a href='http://127.0.0.1:8000/s/'>ID</a> <br> Student Name: {sn}<br> Student Roll Num : {rol}<br> Student Age: {ag}<br>"
    )


def frst(s):
    return render(s, "firstapp/demo.html")


def dsply(request, jk, a):
    return render(request, "firstapp/first.html", {"nm": jk, "ag": a})


def studG(request):
    print(f"Roll number : {request.GET}")
    return render(request, "firstapp/stform.html")


def studP(request):
    print(request.POST)
    if request.method == "POST":
        a = request.POST["rn"]
        b = request.POST["stn"]
        c = request.POST["age"]
        d = request.POST["eml"]
        e = request.POST["Gen"]
        # print( f"Roll number : {request.POST}")
        return render(
            request,
            "firstapp/display.html",
            {"roll": a, "sname": b, "age": c, "mail": d, "Gen": e},
        )
    return render(request, "firstapp/sformpost.html")


def boot(self):
    return render(self, "firstapp/bt.html")


def regform(self):
    return render(self, "firstapp/regiform.html")


def static(self):
    return render(self, "firstapp/Staticdemo.html")


def boots(self):
    return render(self, "firstapp/boots.html")


def crud(request):
    p = Student.objects.all()
    if request.method == "POST":
        a = request.POST["r"]
        b = request.POST["n"]
        c = request.POST["y"]
        d = request.POST["b"]
        w = Student.objects.create(roll=a, sname=b, year=c, branch=d)
        return redirect("/")
    return render(request, "firstapp/crud.html", {"v": p})


def stupdate(self, k):
    return render(self, "firstapp/stupdate.html")

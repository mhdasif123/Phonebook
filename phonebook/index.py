from django.shortcuts import render

def webpage1(request):
    return render(request,"newcontact.html")
def webpage2(request):
    return render(request,"display.html")
def webpage3(request):
    return render(request,"update.html")
def webpage4(request):
    return render(request,"delete.html")
def mainpage(request):
    return render(request,"home.html")
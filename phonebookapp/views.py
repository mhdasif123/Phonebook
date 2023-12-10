from django.shortcuts import render
from.models import Phonebook

# Create your views here.

def fun1(request):
    return render(request,"home.html")

def fun2(request):
    return render(request,"newcontact.html")

def fun3(request):
    return render(request,"display.html")

def fun4(request):
    return render(request,"update.html")

def fun5(request):
    return render(request,"delete.html")


# Add new Contact

def insert(request):
    ph={} 
    name=request.POST["name"]
    number=request.POST["mobilenumber"]
    contactlist=Phonebook(Name=name,Number=number)
    if not name or not number:
        ph["key1"] = "Name and mobile number are added."
        return render(request, "newcontact.html", ph)

    if Phonebook.objects.filter(Number=number).exists():
        ph["key1"] = "Contact with this number already exists."
        return render(request, "newcontact.html", ph)
    contactlist.save()
    ph["key1"]="Contact details added..."
    return render(request,"newcontact.html",ph)

    

# display contact

def display(request):
    contactdetails=Phonebook.objects.all()
    return render(request,"display.html",{"contact":contactdetails})


# Update Conatct

def update(request):
    try:
        oldname=request.POST["oldname"]
        newname=request.POST["newname"]
        if oldname==newname:
            return render(request,"update.html",{"key3":" Contact already exist..."})
        else:
            updated=Phonebook.objects.filter(Name=oldname).update(Name=newname)
            if updated==0:
                return render(request,"update.html",{"key3":"Contact not found in the contact list..."})
            else:
                return render(request, "update.html", {"key3": "Contact Updated..."})
    except Exception as c:
        print(c)
        return render(request,"update.html",{"key3":"Contact not updated..."})
    
# Contact Updated

def updatenumber(request):
    try:
        oldnumber=request.POST["oldnumber"]
        newnumber=request.POST["newnumber"]
        if oldnumber==newnumber:
            return render(request,"update.html",{"key5":" Contact already exist..."})
        else:
            updated=Phonebook.objects.filter(Number=oldnumber).update(Number=newnumber)
            if updated==0:
                return render(request,"update.html",{"key5":"Contact not found in the contact list..."})
            else:
                return render(request, "update.html", {"key5": "Contact Updated..."})
    except Exception as e:
        print(e)
        return render(request,"update.html",{"key5":"Contact not updated..."})

# Delete Contact

def delete(request):
    try:
        dltname=request.POST["name"]
        dltnumber=request.POST["number"]
        delete_count=Phonebook.objects.filter(Name=dltname,Number=dltnumber).delete()
        if delete_count[0]==0:
            return render(request,"delete.html",{"key4":"Contact not found in the contact list..."})
        else:
            return render(request, "delete.html", {"key4": "Name Deleted..."})
    except Exception as d:
        print(d)
        return render(request,"delete.html",{'key4':'Name Not Deleted...'})
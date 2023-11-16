from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import student

def home(request):
    data =student.objects.all()
    context={'dat':data}
    return render(request, 'index.html',{'data':data})

def about(request):
    return render(request, '/')

def handlesignup(request):
    if request.method == 'Post':
        username = request.POST.get("username")
        password = request.POST.get("password")

        myuser = User.objects.create_user(username, password)
        myuser.save()
    return render(request,'signup.html')

def handlelogin(request):
    if request.method== 'POST':
        username=request.POST.get("username")
        password= request.POST.get("password")
        myuser= authenticate(username=username,password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('/')
        else :
            return redirect('/login')
    return render(request, "login.html")

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        # print(name,email,age,gender)
        query = student(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")

    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit = student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.gender = gender
        edit.age = age
        edit.save()
        return redirect("/")

    d = student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)


def deleteData(request, id):
    d = student.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request, "index.html")
def handlelogout(request):
    logout(request)
    return redirect('/signup')

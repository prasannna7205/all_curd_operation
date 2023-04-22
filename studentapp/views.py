from django.shortcuts import render,redirect
from .models import StudentData

def mainpage(request):
    student=StudentData.objects.all()
    return render(request,'mainpage.html',{'student':student})
def add_student(request):
    if request.method == 'GET':
        return render(request,'add_student.html')
    else:
        StudentData(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            course=request.POST['course'],
            ).save()
        return redirect(mainpage)

def update(request,id):
    if request.method == 'GET':
        return render(request,'update.html',{'id':id})
    else: 
        Student=StudentData.objects.get(id=id)
        Student.first_name=request.POST['fname']
        Student.last_name=request.POST['lname']
        Student.email=request.POST['email']
        Student.mobile=request.POST['mobile']
        Student.course=request.POST['course']
        Student.save()
        return redirect(mainpage)
def delete(request,id):
    Student=StudentData.objects.get(id=id)
    Student.delete()
    return redirect(mainpage)
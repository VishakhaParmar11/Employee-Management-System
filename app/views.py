from django.shortcuts import render,redirect
from .models import * 
from django.contrib import messages

# Create your views here.

def EmployeeInsertPage(request):
    return render(request,"app/emp_insert.html")

def InsertEmpData(request):
    if request.method == "POST":
        emp_name = request.POST.get('emp_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        emp_dept = request.POST.get('emp_dept')
        salary = request.POST.get('salary')
        photo = request.FILES.get('photo')

        employee.objects.create(
            emp_name=emp_name,
            gender=gender,
            dob=dob,
            email=email,
            address=address,
            contact=contact,
            emp_dept=emp_dept,
            salary=salary,
            photo=photo
        )

        return redirect('displaydata')

    return redirect('emppage')

def ShowEmployeeData(request):
      all_data = employee.objects.all()
      return render(request,"app/emp_display.html",{'key1':all_data})

def EditPage(request,pk):
     get_data = employee.objects.get(id=pk)
     return render(request,"app/emp_update.html",{'key2':get_data})

def UpdateInfo(request,pk):
     emp = employee.objects.get(id=pk)

     if request.method == "POST":
        emp.emp_name = request.POST.get('emp_name')
        emp.gender = request.POST.get('gender')
        emp.dob = request.POST.get('dob')
        emp.email = request.POST.get('email')
        emp.address = request.POST.get('address')
        emp.contact = request.POST.get('contact')
        emp.emp_dept = request.POST.get('emp_dept')
        emp.salary = request.POST.get('salary')
        
        if 'photo' in request.FILES:
            emp.photo = request.FILES['photo']

        emp.save()
        return redirect('displaydata')
     
     return render(request,"app/emp_update.html",{'key2':emp})

def DeleteData(request,pk):
    del_data = employee.objects.get(id=pk)
    del_data.delete()
    return redirect('displaydata')
from django.shortcuts import render
from .models import Employee
from django.http import HttpResponseRedirect
# Create your views here.

def employee_list(request):
	detail = Employee.objects.all()
	context = {
		'employee_list':detail
	}
	return render(request,"empdetails/emp_list.html",context)



def employee_detail(request,id):
	each_employee = Employee.objects.get(id=id)
	context = {
		'employee_detail':each_employee
	}
	return render(request,"empdetails/emp_details.html",context)


def employee_delete(request,id):
	each_employee = Employee.objects.get(id=id)
	each_employee.delete()
	return HttpResponseRedirect('/emp/')

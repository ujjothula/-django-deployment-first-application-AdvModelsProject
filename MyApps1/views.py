from django.shortcuts import render
from MyApps1.models import Employees
from django.shortcuts import render
from MyApps1.models import Employees, ProxyEmployees1,ProxyEmployees2
# Create your views here.

def display_view(request):
	employees = Employees.objects.all();
	#employees = Employees.objects.get_emp_sal_range(3000,5000)
	#employees = Employees.objects.get_employees_sorted_by('esal')
	#employees = Employees.objects.get_employees_sorted_by('-esal')
	#employees = Employees.objects.get_employees_sorted_by('eaddr')
	#employees = Employees.objects.get_employees_sorted_by('-eaddr')
	#employees = Employees.objects.get_employees_sorted_by('ename')
	#employees = Employees.objects.get_employees_sorted_by('-ename')
	dict1 = {'employees':employees}
	return render(request,'MyApps1/index.html',dict1)


def display_view2(request):
	employees = Employees.objects.all()
	employees = ProxyEmployees1.objects.all()
	employees = ProxyEmployees2.objects.all()
	dict1 = {'employees':employees}
	return render (request ,'MyApps1/index.html' , dict1)

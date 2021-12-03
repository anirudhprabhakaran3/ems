from django.shortcuts import render, redirect, get_object_or_404

import employees
from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm

# Create your views here.

def index(request):
    return render(request, 'employees/index.html')

def list_employees(request):
    employees = Employee.objects.all()
    args = {
        'employees': employees
    }
    return render(request, 'employees/list_employees.html', args)

def list_departments(request):
    departments = Department.objects.all()
    args = {
        'departments': departments
    }
    return render(request, 'employees/list_departments.html', args)

def employee_details(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    args = {
        'employee': employee
    }
    return render(request, 'employees/employee_details.html', args)

def department_details(request, department_id):
    department = Department.objects.get(id=department_id)
    args = {
        'department': department
    }
    return render(request, 'employees/department_details.html', args)

def new_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('employee_details', employee_id=employee.id)
    else:
        form = EmployeeForm()
    args = {
        'form': form
    }
    return render(request, 'employees/employee_form.html', args)

def new_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return redirect('department_details', department_id=department.id)
    else:
        form = DepartmentForm()
    args = {
        'form': form
    }
    return render(request, 'employees/department_form.html', args)

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('employee_details', employee_id=employee.id)
    else:
        form = EmployeeForm(instance=employee)
    args = {
        'form': form
    }
    return render(request, 'employees/employee_form.html', args)

def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            department = form.save(commit=False)
            department.save()
            return redirect('department_details', department_id=department.id)
    else:
        form = DepartmentForm(instance=department)
    args = {
        'form': form
    }
    return render(request, 'employees/department_form.html', args)


def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect(request, 'index')

def delete_department(request, department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    return redirect(request, 'list_departments')
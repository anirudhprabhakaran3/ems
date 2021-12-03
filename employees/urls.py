from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # List
    path('employees', views.list_employees, name='list_employees'),
    path('departments', views.list_departments, name='list_departments'),
    # Read
    path('employees/<int:employee_id>', views.employee_details, name='employee_details'),
    path('departments/<int:department_id>', views.department_details, name='department_details'),
    # Create
    path('employees/new', views.new_employee, name='new_employee'),
    path('department/new', views.new_department, name='new_department'),
    # Update
    path('employees/<int:employee_id>/edit', views.edit_employee, name='edit_employee'),
    path('departments/<int:department_id>/edit', views.edit_department, name='edit_department'),
    # Delete
    path('employees/<int:employee_id>/delete', views.delete_employee, name='delete_employee'),
    path('departments/<int:department_id>/delete', views.delete_department, name='delete_department'),
]
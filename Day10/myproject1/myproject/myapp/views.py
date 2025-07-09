from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Employee

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['title', 'author', 'publication_date']
    template_name = 'Employee_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('Employee_list')  # URL to redirect to after successful form submission

class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'Employee'  # Optional: specify the context variable name in templates
    template_name = 'Employee_list.html'  # Optional: specify custom template

class EmployeeUpdateView(UpdateView):
    model =Employee
    fields = ['title', 'author', 'publication_date']
    template_name = 'Employee_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('Employee_list')  # URL to redirect to after successful form submission

class EmployeeDeleteView(DeleteView):
    model =Employee
    template_name = 'Employee_confirm_delete.html'  # Optional: specify custom template
    success_url = reverse_lazy('Employee_list')  # URL to redirect to after successful deletion


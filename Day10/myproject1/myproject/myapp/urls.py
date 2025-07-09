from django.urls import path
from .views import EmployeeCreateView,EmployeeListView
from .views import EmployeeUpdateView, EmployeeDeleteView
urlpatterns = [
    path('', EmployeeListView.as_view(), name='Employee_list'),
    path('create/', EmployeeCreateView.as_view(), name='Employee_create'),
    path('update/<int:pk>/', EmployeeUpdateView.as_view(), name='Employee_update'),
    path('delete/<int:pk>/', EmployeeDeleteView.as_view(), name='Employee_delete'),
]
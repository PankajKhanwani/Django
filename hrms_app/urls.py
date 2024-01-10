from django.urls import path
from .views import EmployeeListCreateView, EmployeeDetailView, AttendanceListCreateView, AttendanceDetailView,\
    EmployeeAttendanceListView, department_report

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
    path('employees/<int:employee_id>/attendance/', EmployeeAttendanceListView.as_view(),
         name='employee-attendance-list'),
    path('department-report/', department_report, name='department-report'),

]

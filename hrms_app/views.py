from django.shortcuts import render
from rest_framework import generics
from .models import Employee, Attendance
from django.db.models import Count
from .serializers import EmployeeSerializer, AttendanceSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class EmployeeAttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Attendance.objects.filter(employee_id=employee_id)

def department_report(request):
    # Use Django's ORM to get the count of employees in each department
    department_counts = Employee.objects.values('department').annotate(employee_count=Count('id'))

    return render(request, 'department_report.html', {'department_counts': department_counts})
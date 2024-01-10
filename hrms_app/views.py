from django.shortcuts import render
from rest_framework import generics
from .models import Employee, Attendance
from django.db.models import Count
from .serializers import EmployeeSerializer, AttendanceSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    """
    List all employees, or create a new employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceListCreateView(generics.ListCreateAPIView):
    """
    List all attendances, or create a new attendance.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an attendance.
    """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class EmployeeAttendanceListView(generics.ListAPIView):
    """
    List all attendances for an employee.
    """
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        """
        Retrieve all attendances for an employee.
        :return: List of attendances for an employee.
        """
        employee_id = self.kwargs['employee_id']
        return Attendance.objects.filter(employee_id=employee_id)


def department_report(request):
    """
    Generate department report.
    :return: HTML report.
    """
    department_counts = Employee.objects.values('department').annotate(employee_count=Count('id'))

    return render(request, 'department_report.html', {'department_counts': department_counts})

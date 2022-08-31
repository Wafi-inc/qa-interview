import requests
from rest_framework.response import Response
from employee.models import Employee
from rest_framework import status
from rest_framework.decorators import api_view
from employee.forms  import  EmployeeSerializer
from django.shortcuts import get_object_or_404



@api_view(['GET','POST','PUT','DELETE'])
def getAll(request,id=None):  
    if request.method == 'GET':
        if id:
          employee = Employee.objects.get(id=id)  
          serializer = EmployeeSerializer(data=employee)
          print(serializer.is_valid())
          return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        employees = Employee.objects.all()
        print(employees)

        serializer = EmployeeSerializer(data=employees, many=True)
        print(serializer.is_valid())
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee = get_object_or_404(Employee, id=id)
        return Response({"status": "success", "data": "Item Deleted"})
    elif request.method == 'PUT':
        employee = Employee.objects.get(id=id)  
        return Response({"status": "success"})
    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




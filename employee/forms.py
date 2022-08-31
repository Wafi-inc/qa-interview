from django import forms  
from employee.models import Employee  
from rest_framework import serializers

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"  

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=20)  
    name = serializers.CharField(max_length=100)  
    email = serializers.EmailField()  
    Phone_Number = serializers.CharField(max_length=15)  
    class Meta:
        model = Employee  
        fields = "__all__"
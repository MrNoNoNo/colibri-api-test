from rest_framework import serializers
from .models import Employee


class EmployeeItemSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    gender = serializers.CharField(max_length=1)

    class Meta:
        model = Employee
        fields = '__all__'


class AgePerIndustrySerializer(serializers.ModelSerializer):  # average age per industry
    class Meta:
        model = Employee
        fields = ('industry', 'date_of_birth')


class SalariesPerIndustrySerializer(serializers.ModelSerializer): # average salaries per industry
    class Meta:
        model = Employee
        fields = ('industry', 'salary')


class SalariesPerExperienceSerializer(serializers.ModelSerializer): # average salary per years of experience
    class Meta:
        model = Employee
        fields = ('years_of_experience', 'salary')


class SalariesPerGenderSerializer(serializers.ModelSerializer): # average salary per gender
    class Meta:
        model = Employee
        fields = ('salary', 'gender')

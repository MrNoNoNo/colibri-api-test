from unittest.mock import patch

from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from api.models import Employee
from api.serializers import *


class EmployeeApiTest(APITestCase):

    @classmethod
    def setUp(self):
        self.first_name = 'John'
        self.last_name = 'Doe'
        self.gender = 'M'
        self.salary = 22222
        self.years_of_experience = 22
        self.email = 'john@doe.com'
        self.date_of_birth = '01/01/1999'
        
        self.url = reverse('employees-list')
        self.client = APIClient()

        self.employee = Employee.objects.create(
            id=1, 
            first_name=self.first_name,
            last_name=self.last_name,
            gender=self.gender,
            years_of_experience=self.years_of_experience,
            email=self.email,
            date_of_birth=self.date_of_birth
        )

    def test_list_employees(self):

        employees = Employee.objects.all()
        expected_data = EmployeeItemSerializer(employees, many=True).data

        response = self.client.get(self.url)
        
        assert response.status_code == 200
        assert response.data['results'] == expected_data


    def test_get_employee(self):
        employee = Employee.objects.first()
        url = reverse('employees-detail', args=[employee.id])

        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data['first_name'] == 'John'
        assert response.data['last_name'] == 'Doe'


    def test_update_employee(self):
        
        employee = Employee.objects.first()
        url = reverse('employees-detail', args=[employee.id])
        data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'test@email.com', 'gender': 'M', 'date_of_birth': '01/01/1999'}

        response = self.client.put(url, data)

        assert response.status_code == 200
        assert response.data['first_name'] == 'John'
        assert response.data['last_name'] == 'Doe'


    def test_delete_employee(self):
        employee = Employee.objects.first()
        url = reverse('employees-detail', args=[employee.id])

        response = self.client.delete(url)

        assert response.status_code == 204


class AverageAgePerIndustryTest(APITestCase):

    @classmethod
    def setUp(self):
        
        self.url = reverse('average-age-per-industry-list')
        self.client = APIClient()

    def test_list_average_age_per_industry(self):
    
        employees = Employee.objects.all().values('date_of_birth','industry')
        expected_data = AgePerIndustrySerializer(employees, many=True).data
        
        with patch('api.views.generate_dataframe') as mock_generate_dataframe:
            mock_generate_dataframe.return_value = expected_data
            response = self.client.get(self.url)
            assert response.status_code == 200
            assert response.data == expected_data


class AverageSalariesPerIndustryTest(APITestCase):

    @classmethod
    def setUp(self):
            
        self.url = reverse('lowest-salaries-per-industry-list')
        self.client = APIClient()
    
    def test_list_average_salaries_per_industry(self):
        
        employees = Employee.objects.all().values('salary','industry')
        expected_data = SalariesPerIndustrySerializer(employees, many=True).data
        
        with patch('api.views.generate_dataframe') as mock_generate_dataframe:
            mock_generate_dataframe.return_value = expected_data
            response = self.client.get(self.url)
            assert response.status_code == 200
            assert response.data == expected_data


class AverageSalariesPerExperienceTest(APITestCase):

    @classmethod
    def setUp(self):
                
        self.url = reverse('average-salaries-per-experience-list')
        self.client = APIClient()

    def test_list_average_salaries_per_experience(self):
            
        employees = Employee.objects.all().values('salary','years_of_experience')
        expected_data = SalariesPerExperienceSerializer(employees, many=True).data
        
        with patch('api.views.generate_dataframe') as mock_generate_dataframe:
            mock_generate_dataframe.return_value = expected_data
            response = self.client.get(self.url)
            assert response.status_code == 200
            assert response.data == expected_data


class AverageSalariesPerGenderTest(APITestCase):
    
    @classmethod
    def setUp(self):
        self.url = reverse('highest-salaries-per-gender-list')
        self.client = APIClient()

    def test_list_average_salaries_per_gender(self):
        employees = Employee.objects.all().values('salary', 'gender')
        expected_data = SalariesPerGenderSerializer(employees, many=True).data
        
        with patch('api.views.generate_dataframe') as mock_generate_dataframe:
            mock_generate_dataframe.return_value = expected_data
            response = self.client.get(self.url)
            assert response.status_code == 200
            assert response.data == expected_data
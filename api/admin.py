from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):  
    list_display = ('id', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'industry', 'salary', 'years_of_experience')

admin.site.register(Employee, EmployeeAdmin)
from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    date_of_birth = models.CharField(max_length=50, blank=True)
    industry = models.CharField(max_length=254, null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

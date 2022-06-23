from rest_framework import viewsets, mixins, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

import pandas as pd
from datetime import datetime

from .serializers import *
from .pagination import CustomNumberPagination
from .models import Employee


def generate_dataframe(
        queryset,
        group_by: str = None,
        agg_param: str = None,
        agg_func: str = None,
        calculate_age: bool = False,
    ):
    """
    Generate a dataframe from a queryset.
    :param queryset: queryset to generate the dataframe from
    :param group_by: group by parameter
    :param agg_param: aggregation parameter
    :param agg_func: aggregation function
    :param calculate_age: checks if it's necessary to calculate the age
    """
    
    birth_column = 'date_of_birth'
    
    df = pd.DataFrame(list(queryset))
    
    if calculate_age:
        current_year = datetime.now().year
        df[birth_column] = pd.to_datetime(df[birth_column])
        df['age'] = df['date_of_birth'].apply(lambda x: current_year - x.year)
    
    df = df.groupby(group_by).agg({agg_param: agg_func}).round(2)


    return df.to_dict()


class EmployeesViewSet(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet
):
    """
    ViewSet for the Employees API.
    Allowed methods: GET, PUT, DELETE.
    """
    serializer_class = EmployeeItemSerializer
    pagination_class = CustomNumberPagination

    queryset = Employee.objects.all().order_by('id')

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'first_name': ['exact','icontains'],
        'last_name': ['exact','icontains'],
        'email': ['exact'],
        'gender': ['exact']
    }

    search_fields = ['first_name', 'last_name', 'email', 'gender', 'industry']


class AverageAgePerIndustryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the average age per industry.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('date_of_birth', 'industry')
    serializer_class = AgePerIndustrySerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='industry', agg_param='age', agg_func='mean', calculate_age=True)
        return Response(df)


class HighestAgePerIndustryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the highest age per industry.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('date_of_birth', 'industry')
    serializer_class = AgePerIndustrySerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='industry', agg_param='age', agg_func='max', calculate_age=True)
        return Response(df)


class LowestAgePerIndustryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the lowest age per industry.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('date_of_birth', 'industry')
    serializer_class = AgePerIndustrySerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='industry', agg_param='age', agg_func='min', calculate_age=True)
        return Response(df)


class AverageSalariesPerIndustryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the average salaries per industry.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('salary', 'industry')
    serializer_class = SalariesPerIndustrySerializer
    
    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='industry', agg_param='salary', agg_func='mean')
        return Response(df)


class HighestSalariesPerIndustryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the highest salaries per industry.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('salary', 'industry')
    serializer_class = SalariesPerIndustrySerializer
    
    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='industry', agg_param='salary', agg_func='max')
        return Response(df)


class LowestSalariesPerIndustryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the lowest salaries per industry.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('salary', 'industry')
    serializer_class = SalariesPerIndustrySerializer
    
    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='industry', agg_param='salary', agg_func='min')
        return Response(df)


class AverageSalariesPerGenderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the average salaries per gender.
    Allowed methods: GET.
    """ 
    queryset = Employee.objects.all().values('salary', 'gender')
    serializer_class = SalariesPerGenderSerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='gender', agg_param='salary', agg_func='mean')
        return Response(df)


class HighestSalariesPerGenderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the highest salaries per gender.
    Allowed methods: GET.
    """
    serializer_class = SalariesPerGenderSerializer
    queryset = Employee.objects.all().values('salary', 'gender')

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='gender', agg_param='salary', agg_func='max')
        return Response(df)


class LowestSalariesPerGenderViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the lowest salaries per gender.
    Allowed methods: GET.
    """
    serializer_class = SalariesPerGenderSerializer
    queryset = Employee.objects.all().values('salary', 'gender')

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='gender', agg_param='salary', agg_func='min')
        return Response(df)


class AverageSalariesPerExperienceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the average salaries per experience.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('salary', 'years_of_experience')
    serializer_class = SalariesPerExperienceSerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='years_of_experience', agg_param='salary', agg_func='mean')
        return Response(df)


class LowestSalariesPerExperienceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the lowest salaries per experience.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('salary', 'years_of_experience')
    serializer_class = SalariesPerExperienceSerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='years_of_experience', agg_param='salary', agg_func='min')
        return Response(df)


class HighestSalariesPerExperienceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet for the highest salaries per experience.
    Allowed methods: GET.
    """
    queryset = Employee.objects.all().values('salary', 'years_of_experience')
    serializer_class = SalariesPerExperienceSerializer

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        df = generate_dataframe(queryset, group_by='years_of_experience', agg_param='salary', agg_func='max')
        return Response(df)
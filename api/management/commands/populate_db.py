import json
from django.core.management.base import BaseCommand, CommandError  # CommandError is a subclass of Exception
from api.models import Employee


class Command(BaseCommand): # subclass BaseCommand

    help = 'Populate the database with data from a JSON file'   # run python manage.py populate_db help to see the help text
    
    def add_arguments(self, parser) -> None:    # add_arguments is a method of BaseCommand
        parser.add_argument('json_file', nargs='+', type=str)   # nargs='+' means that the user can pass more than one argument
        return super().add_arguments(parser)               # super() is a method of BaseCommand

    def handle(self, *args, **options) -> None: # handle is a method of BaseCommand
        with open(options['json_file'][0]) as json_file:    # open the file passed in as an argument
            data = json.load(json_file)                    # load the JSON data into a Python object
        
        for record in data:                           # iterate over the records
            record['pk'] = record['id']             # add a primary key to the record
            Employee.objects.get_or_create(**record)    # get or create an Employee object
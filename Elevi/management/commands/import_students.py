
import pandas as pd
import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Elevi.models import Elevi, Class

class Command(BaseCommand):
    help = 'Import students from an Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            df = pd.read_excel(file_path)
            for index, row in df.iterrows():
                class_name = row['class_number']
                class_obj, created = Class.objects.get_or_create(name=class_name)
                
                first_name = row['first_name']
                last_name = row['last_name']
                email = row['email']
                
                # Generate a username based on the pattern FirstName_LastName_2randomnumbers
                username_base = f"{first_name}_{last_name}"
                username = self.generate_unique_username(username_base)
                
                # Create a User object
                user = User.objects.create_user(username=username, email=email, password='defaultpassword123')
                user.first_name = first_name
                user.last_name = last_name
                user.save()

                # Create an Elev object
                Elevi.objects.create(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    class_number=class_obj
                )
            self.stdout.write(self.style.SUCCESS('Successfully imported students from Excel file'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing students: {e}'))

    def generate_unique_username(self, base):
        while True:
            username = f"{base}_{random.randint(10, 99)}"
            if not User.objects.filter(username=username).exists():
                return username

import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Generate random users'

    def handle(self, *args, **kwargs):
        num_users = 100
        faker = Faker()

        for _ in range(num_users):
            # Generate random user data
            username = faker.user_name()
            email = faker.email()
            password = faker.password()

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = faker.first_name()
            user.last_name = faker.last_name()
            user.save()

            self.stdout.write(self.style.SUCCESS(f'Created user: {username}, Email: {email}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_users} users.'))

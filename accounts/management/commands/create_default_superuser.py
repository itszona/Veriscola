from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Obviously, this is a test project, and as such
# Privacy/security, are not major concerns
# In a production app, effort must be made to conceal
# credentials, in environment variables or similar
USERNAME = "testmaster"
PASSWORD = "testmaster"


class Command(BaseCommand):
    help = "Create a superuser with a simple password"

    def handle(self, *args, **options):
        User: AbstractUser = get_user_model()

        if not User.objects.filter(username=USERNAME).exists():
            User.objects.create_superuser(username=USERNAME, password=PASSWORD)
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
        else:
            self.stdout.write(
                self.style.ERROR(
                    "A user with this username already exists. Superuser not created."
                )
            )

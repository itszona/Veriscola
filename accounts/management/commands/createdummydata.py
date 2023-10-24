from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from accounts.models import (
    Course,
    Student,
    Staff,
    CustomUser,
    StaffTypes,
    STUDENT_LEVELS,
)

import faker
from faker import Faker

fake = faker.Faker()

NO_RECORDS = 15


class Command(BaseCommand):
    help = "Create a large amount of dummy data in the database for testing and visualization"

    def handle(self, *args, **options):
        # Create dummy users
        ...

    def create_dummy_courses(self):
        courses = [
            Course(
                name=fake.name(),
                code=fake.pystr(max_chars=5),
            )
            for _ in range(NO_RECORDS)
        ]
        new_courses = Course.objects.bulk_create(courses)
        self.stdout.write(
            self.style.SUCCESS(f"Number of new courses: {len(new_courses)}")
        )

    def create_dummy_staff(self):
        for _ in range(NO_RECORDS):
            user = CustomUser.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                first_name=fake.person.first_name(),
                last_name=fake.person.last_name(),
            )
            staff_type = fake.random_element(StaffTypes.values)
            department = fake.word()
            Staff.objects.create(
                _user=user, staff_type=staff_type, department=department
            )
            self.stdout.write(
                self.style.SUCCESS(f"Staff created: {user.username} ({staff_type})")
            )

    def create_dummy_students(self):
        fake = Faker()
        User = get_user_model()
        for _ in range(NO_RECORDS):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                first_name=fake.person.first_name(),
                last_name=fake.person.last_name(),
            )
            department = fake.word()
            level = fake.random_element(STUDENT_LEVELS)
            student_picture = "uploads/student-images/default.jpg"
            Student.objects.create(
                _user=user,
                department=department,
                level=level,
                student_picture=student_picture,
            )
            self.stdout.write(
                self.style.SUCCESS(f"Student created: {user.username} ({level})")
            )

from django.db import models
from django.contrib.auth import get_user_model

STUDENT_IMAGE_UPLOAD_PATH = "static/uploads/student-images"


class StudentLevels(models.TextChoices):
    L100 = "100L"
    L200 = "200L"
    L300 = "300L"
    L400 = "400L"
    L500 = "500L"
    NA = "NA"


STUDENT_LEVELS = (
    ("100L", "100L"),
    ("200L", "200L"),
    ("300L", "300L"),
    ("400L", "400L"),
    ("500L", "500L"),
    ("NA", "NA"),
)


class Student(models.Model):
    name = models.CharField(max_length=250, blank=True)
    registration_no = models.CharField(max_length=20, unique=True)
    department = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Faculty and department of the student",
    )
    level = models.CharField(
        max_length=10, choices=STUDENT_LEVELS, default=StudentLevels.L100
    )
    courses = models.ManyToManyField(
        to="accounts.Course",
        related_name="students",
        related_query_name="student",
        blank=True,
    )
    student_picture = models.ImageField(upload_to=STUDENT_IMAGE_UPLOAD_PATH)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

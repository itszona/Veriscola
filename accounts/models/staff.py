from django.db import models
from django.contrib.auth import get_user_model


class StaffTypes(models.TextChoices):
    LECTURER = "LECTURER"
    NON_ACADEMIC = "NON_ACADEMIC"
    EMERITUS = "EMERITUS"
    MANAGEMENT = "MANAGEMENT"


class Staff(models.Model):
    _user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name="staff",
        related_query_name="staff",
    )
    staff_type = models.CharField(
        max_length=20, choices=StaffTypes.choices, help_text="Type/nature of staff"
    )
    department = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Faculty and department of the staff",
    )
    courses = models.ManyToManyField(
        to="accounts.Course",
        related_name="lecturers",
        related_query_name="lecturer",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self._user.first_name} {self._user.last_name}"

    class Meta:
        verbose_name = "staff"
        verbose_name_plural = "staff"

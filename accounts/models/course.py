from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="Course name e.g Strength of Materials II",
    )
    code = models.CharField(
        max_length=8,
        help_text="A short code description e.g MEE203",
        unique=True,
    )

    def __str__(self) -> str:
        return self.name

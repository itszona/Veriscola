# Generated by Django 4.2.6 on 2023-10-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_student_department_alter_student_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="code",
            field=models.CharField(
                help_text="A short code description e.g MEE203",
                max_length=8,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="name",
            field=models.CharField(
                help_text="Course name e.g Strength of Materials II", max_length=30
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="courses",
            field=models.ManyToManyField(
                blank=True,
                related_name="lecturers",
                related_query_name="lecturer",
                to="accounts.course",
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(
                blank=True,
                related_name="students",
                related_query_name="student",
                to="accounts.course",
            ),
        ),
    ]

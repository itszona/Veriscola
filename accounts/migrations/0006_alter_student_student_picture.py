# Generated by Django 4.2.6 on 2023-10-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "accounts",
            "0005_remove_student__user_student_created_at_student_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_picture",
            field=models.ImageField(upload_to="static/uploads/student-images"),
        ),
    ]
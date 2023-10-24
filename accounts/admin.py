from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Course, Student, Staff, StudentLevels, CustomUser


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    ...


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    ...


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    ...


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    ...

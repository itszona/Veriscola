from django import forms
from accounts.models import Student, Course, Staff


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


# class CourseForm(forms.ModelForm):
#     class Meta:
#         model =

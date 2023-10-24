from typing import Any
from django import http
from django.db import models
from django.db.models import QuerySet, Model
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Course, Student, StudentLevels
from accounts.forms import StudentForm
from django.shortcuts import redirect
from django.urls import reverse


#import barcode
#from django.core.exceptions import ObjectDoesNotExist
#from escpos.printer import Network


import os
#from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import barcode   
from barcode.writer import ImageWriter 
from django.http import HttpResponse
#from escpos.printer import Usb









class StudentListView(ListView):
    model = Student
    template_name = "accounts/student_list.html"


class IndexView(TemplateView):
    template_name = "accounts/index.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Add a list of all courses to the context
        context["all_courses"] = Course.objects.all()
        context["all_student_levels"] = StudentLevels.values
        return context

    def get(self, request, *args: Any, **kwargs: Any):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        print(data, "\n\n\n")
        data = {k: v[0] for k, v in data.items()}
        courses = data.pop("courses", [])
        if isinstance(courses, str):
            courses = courses.split(",")
        courses = Course.objects.filter(pk__in=courses).all()
        form = StudentForm(data, files=request.FILES)
        if not form.is_valid():
            # Handle form errors
            print(form.errors, "\n\n")
            context = self.get_context_data()
            return JsonResponse({"form_errors": form.errors}, status=404)

        instance = form.save()
        instance.courses.set(courses)
        return redirect(to=reverse("student-list"))
        # redirect to list all students


class StudentListView(ListView):
    model = Student
    template_name = "accounts/student_list.html"


class StudentVerifyView(DetailView):
    template_name = "accounts/verify.html"
    model = Student
    
    
#import barcode
#from barcode.writer import ImageWriter

def generate_barcode(request, code):
    # Generate a barcode SVG using the `python-barcode` library
    ean = barcode.get('ean13', code, writer=ImageWriter(), add_checksum=False)
    barcode_svg = ean.save('media/barcode')  # Save the barcode image

    with open(barcode_svg, 'rb') as f:
        response = HttpResponse(f.read(), content_type="image/svg+xml")

    return response

def barcode_to_pdf(request):
    return render(request, 'barcode.html')
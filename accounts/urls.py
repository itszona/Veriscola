from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("list/", views.StudentListView.as_view(), name="student-list"),
    path("verify/<int:pk>/", views.StudentVerifyView.as_view(), name="student-verify"),
    path('verify/<int:pk>/generate_barcode/<str:code>/', views.generate_barcode, name='generate_barcode'),
    path('verify/<int:pk>/barcode_to_pdf/', views.barcode_to_pdf, name='barcode_to_pdf'),
]

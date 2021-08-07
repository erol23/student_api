from django.urls import path
from .views import home, manuel_api, student_add_api, student_list_api, student_list_api2,student_api

urlpatterns = [
  path('', home),
  # path('student/', manuel_api),
  path('list/', student_list_api),
  path('list2/', student_list_api2),
  path('add/', student_add_api),
  path('student/', student_api),
]

from django.urls import path
from apps.student.views import *

app_name = 'student'

urlpatterns = [
    path('', StudentListView.as_view(), name='student'),
]

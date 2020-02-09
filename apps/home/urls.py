
from django.urls import path
from apps.home.views import *

app_name = 'home'

urlpatterns = [
    path('student', StudentListView.as_view(), name='student'),
    path('teacher', TeacherListView.as_view(), name='teacher'),
    path('save_departmental', save_departmental, name='save_departmental'),
    path('save_practice', save_practices, name='save_practices'),
]

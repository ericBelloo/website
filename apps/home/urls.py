
from django.urls import path
from apps.home.views import *

app_name = 'home'

urlpatterns = [
    path('student', NewHomeworkView.as_view(), name='student'),
    path('teacher', HomeworkListView.as_view(), name='teacher'),
    path('save_departmental', save_departmental, name='save_departmental'),
    path('save_practice', save_practices, name='save_practices'),
    path('save_image', save_image, name='save_image'),
]


from django.urls import path
from apps.home.views import *

app_name = 'home'

urlpatterns = [
    path('student', NewHomeworkView.as_view(), name='student'),
    path('teacher', HomeworkListView.as_view(), name='teacher'),
    path('homework/<int:id_document>', HomeworkView.as_view(), name='homework'),
    path('save_image', save_image, name='save_image'),
    path('get_document/<int:pk>', get_document, name='get_document'),  # get content for each document
    path('get_document_list/<str:value>/', get_document_list, name='get_document_list'),
]

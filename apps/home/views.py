from django.shortcuts import render
from django.views.generic import View, ListView
# Create your views here.


class StudentListView(ListView):
    template_name = 'base.html'

    def get_queryset(self):
        pass

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StudentListView, self).get_context_data()
        context['student'] = True
        return context


class TeacherListView(ListView):
    template_name = 'base.html'

    def get_queryset(self):
        pass

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TeacherListView, self).get_context_data()
        return context

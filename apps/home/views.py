from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from apps.model.models import Documents
# Create your views here.
data = dict()


class StudentListView(View):
    template_name = 'base.html'
    model = Documents

    def get(self, request, *data, **kwargs):
        context = dict()
        context['student'] = True
        context['first_dep'] = self.model.objects.filter(departmental=1)
        context['second_dep'] = self.model.objects.filter(departmental=2)
        context['third_dep'] = self.model.objects.filter(departmental=3)
        context['final_project'] = self.model.objects.filter(departmental=4)
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        files = request.FILES.getlist('file')
        departmental = int(request.POST.get('departmental'), False)
        if departmental:
            for file in files:
                document = Documents.objects.create(name=file.name, file=file, departmental=departmental)
                document.save()
        data['success'] = True
        data['message'] = 'The information has been saved correctly'
        return JsonResponse(data)


class TeacherListView(ListView):
    template_name = 'base.html'
    model = Documents

    def get_queryset(self):
        pass

    def get_context_data(self, object_list=None, **kwargs):
        context = super(TeacherListView, self).get_context_data()
        context['first_dep'] = self.model.objects.filter(departmental=1)
        context['second_dep'] = self.model.objects.filter(departmental=2)
        context['third_dep'] = self.model.objects.filter(departmental=3)
        context['final_project'] = self.model.objects.filter(departmental=4)
        return context

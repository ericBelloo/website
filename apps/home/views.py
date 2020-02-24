from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from apps.model.models import Documents, Practices, Images
# Create your views here.
data = dict()
context = dict()


class NewHomeworkView(View):
    template_name = 'new_homework.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


def save_departmental(request):
    files = request.FILES.getlist('file')
    departmental = int(request.POST.get('departmental'))
    for file in files:
        document = Documents.objects.create(name=file.name, file=file, departmental=departmental)
        document.save()
    data['success'] = True
    data['message'] = 'The information has been saved correctly'
    return JsonResponse(data)


def save_practices(request):
    files = request.FILES.getlist('file')
    for file in files:
        document = Practices.objects.create(name=file.name, file=file)
        document.save()
    data['success'] = True
    data['message'] = 'The information has been saved correctly'
    return JsonResponse(data)


def save_image(request):
    image = request.FILES.get('image', False)
    if image:
        image_object = Images.objects.create(image=image, name=image.name)
        image_object.save()
        data['url'] = image_object.image.url
        data['name'] = image_object.image.name
    return JsonResponse(data)


class HomeworkListView(View):
    """
        Show documents, practices and the project
    """
    template_name = 'homeworks_list.html'

    def get(self, request, **kwargs):
        context['first_departmental'] = Documents.objects.filter(departmental=1).values('title', 'id')
        context['second_departmental'] = Documents.objects.filter(departmental=2).values('title', 'id')
        context['third_departmental'] = Documents.objects.filter(departmental=3).values('title', 'id')
        return render(request, self.template_name, context)


from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, ListView
from apps.model.models import Documents, Practices, Images
# Create your views here.
data = dict()
context = dict()


class NewHomeworkView(View):
    template_name = 'new_homework.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

    def post(self, request, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        departmental = request.POST.get('departmental')
        try:
            document = Documents.objects.create(title=title, content=content, departmental=departmental)
            document.save()
            data['success'] = True
            data['url'] = reverse('home:teacher')
            data['message'] = 'Document saved'
        except Exception as error:
            data['success'] = True
            data['message'] = 'Error saving'
            data['error'] = error.args
        return JsonResponse(data)


def save_image(request):
    image = request.FILES.get('image', False)
    if image:
        image_object = Images.objects.create(image=image, name=image.name)
        image_object.save()
        data['url'] = image_object.image.url
        data['name'] = image_object.image.name
    return JsonResponse(data)


class HomeworkListView(ListView):
    """
        Show documents, practices and the project
    """
    template_name = 'homeworks_list.html'

    def get_queryset(self):
        return Documents.objects.all().values('title', 'id')


class HomeworkView(View):
    template_name = 'homework.html'

    def get(self, request, **kwargs):
        document = Documents.objects.values('id', 'title').get(id=kwargs.get('id_document'))
        context['id'] = document['id']
        context['title'] = document['title']
        return render(request, self.template_name, context)


def get_document(request, pk):
    document = Documents.objects.get(id=pk)
    data['success'] = True
    data['message'] = 'The information has been saved correctly'
    data['html'] = document.content
    return JsonResponse(data)

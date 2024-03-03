from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageModel
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


def testRequest(request):
    # return HttpResponse(render(request,'first.html')) # For Testing Purposes !!
    return HttpResponse('Error!!!')

class ImageList(ListView):
    model = ImageModel
    template_name = 'App1/image_list.html'
    context_object_name = 'media'

class ImageDetail(DetailView):
    model = ImageModel
    context_object_name = "media_id"
    template_name = "App1/media_id.html"

class ImageUpload(CreateView):
    model = ImageModel
    fields = ['image','choice']
    template_name = 'App1/media_upload.html'
    success_url = reverse_lazy('main')

class UpdateImage(UpdateView):
    model = ImageModel
    fields = ['choice']
    template_name = 'App1/media_upload.html'
    success_url = reverse_lazy('main')

class DeleteImage(DeleteView):
    model=ImageModel
    context_object_name = 'delete'
    template_name = 'App1/delete_form.html'
    success_url = reverse_lazy('main')
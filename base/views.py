from io import BytesIO

from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.files.base import ContentFile
from django.http import FileResponse

from .models import Images, OriginalImage
from .forms import ImageForm

from .image_convert import to_sketch

from PIL import Image
import time


# Create your views here.
def download_original(request, pk):
    image = OriginalImage.objects.get(id=pk)
    return FileResponse(image.image.open(), as_attachment=True, filename="original.jpg")


def download_gray(request, pk):
    image = Images.objects.get(id=pk)
    return FileResponse(image.grayscale_img.open(), as_attachment=True, filename="gray.jpg")


def download_sketch(request, pk):
    image = Images.objects.get(id=pk)
    return FileResponse(image.sketch_img.open(), as_attachment=True, filename="sketch.jpg")


class MainView(FormView):
    form_class = ImageForm
    template_name = 'base/index.html'
    success_url = reverse_lazy('image_upload')

    def get(self, request, *args, **kwargs):
        images = Images.objects.all().order_by('-id')[:10]
        form = ImageForm()

        context = {
            'form': form,
            'images': images
        }

        return render(request, self.template_name, context)

    def form_valid(self, form):
        # Save Original Image
        add = form.save()

        # Get original Image path for further conversion
        og_image = OriginalImage.objects.get(id=add.id)
        image_url = og_image.image

        # Opening image and applying convesion operations
        img = Image.open(image_url)
        grayscale_img = img.convert('L')
        sketch_img = to_sketch(img)

        # Save images as files
        gray_img_io = BytesIO()
        grayscale_img.save(gray_img_io, format='JPEG', quality=100)
        gray_img_content = ContentFile(
            gray_img_io.getvalue(), str(int(time.time()))+'.jpg')

        sketch_img_io = BytesIO()
        sketch_img.save(sketch_img_io, format='JPEG', quality=100)
        sketch_img_content = ContentFile(
            sketch_img_io.getvalue(), str(int(time.time()))+'.jpg')

        # Create Images object
        Images.objects.create(
            original_img=og_image, grayscale_img=gray_img_content, sketch_img=sketch_img_content)

        return super(MainView, self).form_valid(form)


class OriginalImageDetail(DetailView):
    model = OriginalImage
    context_object_name = 'image'
    template_name = 'base/original_img.html'


class GrayscaleImageDetail(DetailView):
    model = Images
    context_object_name = 'image'
    template_name = 'base/grayscale_img.html'


class SketchImageDetail(DetailView):
    model = Images
    context_object_name = 'image'
    template_name = 'base/sketch_img.html'

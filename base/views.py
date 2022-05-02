from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.urls import reverse_lazy

from .models import Images
from .forms import ImageForm

from .image_convert import to_sketch

from PIL import Image
import time


# Create your views here.
class MainView(FormView):
    form_class = ImageForm
    template_name = 'base/index.html'
    success_url = reverse_lazy('image_upload')

    def get(self, request, *args, **kwargs):
        images = Images.objects.all().order_by('id').reverse()
        form = ImageForm()

        context = {
            'form': form,
            'images': images
        }

        return render(request, self.template_name, context)

    def form_valid(self, form):
        # Save Original Image and get ID
        add = form.save()
        i_id = add.id

        # From Id get original Image path for further conversion
        og_image = Images.objects.get(id=add.id)
        image_url = og_image.original_img

        # Opening image and applying convesion operation
        img = Image.open(image_url)
        grayscale_img = img.convert('L')
        grayscale_name = int(time.time())
        grayscale_img.save('grayscale/{}.jpeg'.format(grayscale_name))

        sketch_img = to_sketch(img)
        sketch_name = int(time.time())
        sketch_img.save('sketch/{}.jpeg'.format(sketch_name))

        # Updating all data
        Images.objects.filter(id=i_id).update(grayscale_img='grayscale/{}.jpeg'.format(
            grayscale_name), sketch_img='sketch/{}.jpeg'.format(sketch_name))

        return super(MainView, self).form_valid(form)


class OriginalImageDetail(DetailView):
    model = Images
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

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from .views import home, OriginalImageDetail, GrayscaleImageDetail, SketchImageDetail
from .views import MainView, OriginalImageDetail, GrayscaleImageDetail, SketchImageDetail

urlpatterns = [
    #     path('', home, name='image_upload'),
    path('', MainView.as_view(), name='image_upload'),
    path('original_img/<int:pk>/',
         OriginalImageDetail.as_view(), name='original_img'),
    path('grayscale_img/<int:pk>/',
         GrayscaleImageDetail.as_view(), name='grayscale_img'),
    path('sketch_img/<int:pk>/',
         SketchImageDetail.as_view(), name='sketch_img'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

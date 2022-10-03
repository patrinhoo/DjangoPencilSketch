from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='image_upload'),
    path('original_img/<int:pk>/',
         views.OriginalImageDetail.as_view(), name='original_img'),
    path('grayscale_img/<int:pk>/',
         views.GrayscaleImageDetail.as_view(), name='grayscale_img'),
    path('sketch_img/<int:pk>/',
         views.SketchImageDetail.as_view(), name='sketch_img'),
    path('download_original/<int:pk>/',
         views.download_original, name='download_original'),
    path('download_gray/<int:pk>/', views.download_gray, name='download_gray'),
    path('download_sketch/<int:pk>/',
         views.download_sketch, name='download_sketch'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

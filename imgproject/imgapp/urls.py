from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.home, name='image_upload'),
    path('view/', views.img_edit, name='image_edit'),
    path('delete_manipulated_image/<int:image_id>/', views.delete_manipulated_image, name='delete_manipulated_image'),

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


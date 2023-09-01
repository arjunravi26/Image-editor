# admin.py: Register the ManipulatedImage model for admin management
from django.contrib import admin

# Register your models here.
from .models import ManipulatedImages
admin.site.register(ManipulatedImages)




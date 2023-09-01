from django.db import models

# Create your models here.

#models.py: Define the ManipulatedImage model to store image versions and info

class ManipulatedImages(models.Model):
    # Fields to store different versions of the image after enhancements
    original_image = models.ImageField(upload_to='media/')
    enhanced_image = models.ImageField(upload_to='media/')
    edge_detected_image = models.ImageField(upload_to='media/')
    grayscale_image = models.ImageField(upload_to='media/')
    green_channel_image = models.ImageField(upload_to='media/')
    artistic_image = models.ImageField(upload_to='media/')
    colored_image = models.ImageField(upload_to='media/')
    sharpened_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return f"Manipulated Image {self.pk}"

# Method to retrieve URLs of all versions of the image
    def get_all_image_urls(self):
     return [
            self.original_image,
            self.enhanced_image,
            self.edge_detected_image,
            self.grayscale_image,
            self.green_channel_image,
            self.artistic_image,
            self.colored_image,
            self.sharpened_image
        ]

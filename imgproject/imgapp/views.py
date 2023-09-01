from django.shortcuts import render
from .models import ManipulatedImages
from t_img_manipulation.img_enchance import enhance_image
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import os,io,base64
from PIL import Image
def home(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            # Check if the uploaded image is in a supported format
            try:
                uploaded_image = ManipulatedImages(original_image=image)
                uploaded_image.save()

            except IOError:
                return render(request, "index.html", {'error_message': 'Unsupported image format'})
            
            # Redirect to a success page or render a message
    return render(request, "index.html")

def img_edit(request):
    uploaded_image = ManipulatedImages.objects.all().last()
    if uploaded_image:
        path = uploaded_image.original_image.path
        uploaded_image_path = uploaded_image.original_image.url
        enhanced_image= enhance_image(path)
        uploaded_image.delete()
        return render(request, 'image.html', {'manipulated_images': enhanced_image,'uploaded_image_path': uploaded_image_path})
    else:
        # Handle the case where no uploaded image is found
        return render(request, 'image.html', {'images': None, 'manipulated_images': None})

def delete_manipulated_image(request, image_id):
    manipulated_images=ManipulatedImages.objects.all().last()
    image_paths = [
          manipulated_images.original_image.path,
          manipulated_images.enhanced_image.path,
          manipulated_images.edge_detected_image.path,
          manipulated_images.grayscale_image.path,
          manipulated_images.green_channel_image.path ,
          manipulated_images.artistic_image.path,
          manipulated_images.colored_image.path,
          manipulated_images.sharpened_image.path,
    ]
    for path in image_paths:
        if(os.path.exists(path)):
            os.remove(path)
        else:
            raise ValueError("{path} doesnot exist")
    
    manipulated_image = get_object_or_404(ManipulatedImages, pk=image_id)
    try:
        manipulated_image.delete()
        success = True
    except Exception as e:
        success = False

    return JsonResponse({'success': success})

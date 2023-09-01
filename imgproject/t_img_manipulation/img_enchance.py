import numpy as np
import cv2
from django.core.files import File
from imgapp.models import ManipulatedImages
import os
from PIL import Image, ImageEnhance

# from PIL import Image,ImageOps
def enhance_image(image_path):
    try:
        # Load an image using OpenCV
        original_image = cv2.imread(image_path)
        original_image_1=original_image.copy()
        original_image_2=original_image.copy()
        if original_image is None:
            raise ValueError(f"Failed to load the image at path: {image_path}")
        artistic_img = cv2.stylization(original_image_1)

        img=Image.open(image_path)
        enhancer = ImageEnhance.Brightness(img)
        brighter_image = enhancer.enhance(1.2)

        enhancer = ImageEnhance.Contrast(brighter_image)
        contrasted_image = enhancer.enhance(1.25)

        enhancer = ImageEnhance.Color(contrasted_image)
        colored_image = enhancer.enhance(1.15)

        rgb_image_colored = colored_image.convert('RGB')
        # Convert the image to grayscale
        grayscale_image = cv2.cvtColor(original_image_2, cv2.COLOR_RGB2LUV)

        # # Apply a Gaussian blur
        blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

        # # Apply a sharpening filter
        sharpened_image = cv2.addWeighted(grayscale_image, 1.5, blurred_image, -0.5, 0)

        # # Convert the image back to RGB
        rgb_image_sharpened = cv2.cvtColor(sharpened_image, cv2.COLOR_RGB2LUV)

        # Convert the image to grayscale using OpenCV
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        # Perform a simple manipulation - increasing brightness
        brightened_image = gray_image + 50
        brightened_image = np.clip(brightened_image, 0, 255).astype(np.uint8)

        # Perform image enhancements
        enhanced_image = cv2.convertScaleAbs(original_image, alpha=1.2, beta=30)
        edges = cv2.Canny(enhanced_image, threshold1=30, threshold2=70)


        # Save manipulated images to files
        output_path_1 = 'media/media/enhanced_image.jpg'
        output_path_2 = 'media/media/edge_detected_image.jpg'
        output_path_3 = 'media/media/grayscale_image.jpg'
        output_path_4 = 'media/media/green_channel_image.jpg'
        output_path_5 = 'media/media/artistic_img.jpg'
        output_path_6 = 'media/media/colored_img.jpg'
        output_path_7 = 'media/media/sharpened_img.jpg'
        
        cv2.imwrite(output_path_1, enhanced_image)
        cv2.imwrite(output_path_2, edges)
        cv2.imwrite(output_path_3, gray_image)
        cv2.imwrite(output_path_4, original_image[:,:,2])
        cv2.imwrite(output_path_5, artistic_img)
        rgb_image_colored.save(output_path_6)
        cv2.imwrite(output_path_7,rgb_image_sharpened)        

        
        # Save manipulated images to the database
        manipulated_image = ManipulatedImages()
        manipulated_image.original_image.save('original_image.jpg', File(open(image_path, 'rb')))
        manipulated_image.enhanced_image.save('enhanced_image.jpg', File(open(output_path_1, 'rb')))
        manipulated_image.edge_detected_image.save('edge_detected_image.jpg', File(open(output_path_2, 'rb')))
        manipulated_image.grayscale_image.save('grayscale_image.jpg', File(open(output_path_3, 'rb')))
        manipulated_image.green_channel_image.save('green_channel_image.jpg', File(open(output_path_4, 'rb')))
        manipulated_image.artistic_image.save('artistic_img.jpg', File(open(output_path_5, 'rb')))
        manipulated_image.colored_image.save('colored_image.jpg', File(open(output_path_6, 'rb')))
        manipulated_image.sharpened_image.save('sharpened_image.jpg', File(open(output_path_7, 'rb')))
        manipulated_image.save()
        
        if os.path.exists(image_path):
           os.remove(image_path)
        if os.path.exists(output_path_1):
           os.remove(output_path_1)
        if os.path.exists(output_path_2):
           os.remove(output_path_2)
        if os.path.exists(output_path_3):
           os.remove(output_path_3)
        if os.path.exists(output_path_4):
           os.remove(output_path_4)
        if os.path.exists(output_path_5):
           os.remove(output_path_5)
        if os.path.exists(output_path_6):
           os.remove(output_path_6)
        if os.path.exists(output_path_7):
           os.remove(output_path_7)
        return manipulated_image
    
    except Exception as e:
        return None  # Handle exceptions and return None or appropriate value


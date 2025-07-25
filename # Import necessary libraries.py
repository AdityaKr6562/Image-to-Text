# Import necessary libraries
from picamera import PiCamera
from time import sleep
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pyttsx3
import os

# Initialize Camera and Text-to-Speech engine
camera = PiCamera()
tts_engine = pyttsx3.init()

# Set camera and OCR settings
def capture_image(image_path='/home/pi/captured_text.jpg'):
    """Captures an image and saves it to a specified path."""
    camera.start_preview()
    sleep(2)  # Allow time for the camera to adjust
    camera.capture(image_path)
    camera.stop_preview()
    print("Image captured successfully.")

def preprocess_image(image_path):
    """Processes the captured image to improve OCR accuracy."""
    image = Image.open(image_path)
    # Enhance image quality
    image = image.convert('L')  # Convert to grayscale
    image = image.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    processed_path = '/home/pi/processed_image.jpg'
    image.save(processed_path)
    print("Image pre-processed successfully.")
    return processed_path

def extract_text(image_path):
    """Extracts text from the processed image using Tesseract OCR."""
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Extracted Text:", text)
    return text

from PIL import Image
import pytesseract

def read_image_text(image_file):
    img = Image.open(image_file)
    text = pytesseract.image_to_string(img)
    return text

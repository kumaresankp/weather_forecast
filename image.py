import pytesseract 

from PIL import Image 

image_path = r'C:\Users\1tami\Desktop\mineSignature.jpeg'


text = pytesseract.image_to_string(Image.open(image_path))


print(text)


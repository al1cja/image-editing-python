from tkinter import filedialog
from PIL import Image, ImageOps, ImageTk

file_path = ""
MAX_WIDTH = 900
MAX_HEIGHT = 600

def add_image(image_container):
    global file_path
    file_path = filedialog.askopenfilename()

    image = Image.open(file_path)
    update_image(image, image_container)

def select_filter(filter, image_container):
    image = Image.open(file_path)

    if filter == "Black and White":
        image = ImageOps.grayscale(image)

    update_image(image, image_container)

def clear_filters(image_container):
    image = Image.open(file_path)
    update_image(image, image_container)

def update_image(image, image_container):
    image = resize_image(image)

    image_container.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    image_container.image = image
    image_container.create_image(0, 0, image=image, anchor="nw")

def resize_image(image):
    width = image.width
    height = image.height
    ratio = width/height

    if (width > MAX_WIDTH):
        width = MAX_WIDTH
        height = MAX_WIDTH / ratio
    
    if (height > MAX_HEIGHT):
        height = MAX_HEIGHT
        width = MAX_HEIGHT * ratio

    image = image.resize((int(width), int(height)), Image.ANTIALIAS)
    return image

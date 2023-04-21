from tkinter import filedialog
from PIL import Image, ImageOps, ImageTk

file_path = ""

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
    # Todo add resizing
    width = int(image.width / 5)
    height = int(image.height / 5)
    image = image.resize((width, height), Image.ANTIALIAS)

    image_container.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    image_container.image = image
    image_container.create_image(0, 0, image=image, anchor="nw")

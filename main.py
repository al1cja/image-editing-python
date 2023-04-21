import tkinter as tk
from tkinter import ttk

import image_editor

window = tk.Tk()

window.title("Photo Editor")
window.geometry("1000x700")
window.config(bg="white")

tool_container = tk.Frame(window, width=1000, height=100)
tool_container.pack(side="top", fill="x")

add_image_button = tk.Button(tool_container, command=lambda: image_editor.add_image(image_container), text="Add Image", bg="white")
add_image_button.pack(pady=10)

filter_dropdown_label = tk.Label(tool_container, text="Select Filter")
filter_dropdown_label.pack()

filter_dropdown = ttk.Combobox(tool_container, values=["Black and White"])
filter_dropdown.pack()
filter_dropdown.bind("<<ComboboxSelected>>", lambda event: image_editor.select_filter(filter_dropdown.get(), image_container))

clear_filters_button = tk.Button(tool_container, command=lambda: image_editor.clear_filters(image_container), text="Clear filters", bg="white")
clear_filters_button.pack(pady=10)

save_image_button = tk.Button(tool_container, command=image_editor.save_image, text="Save", bg="white")
save_image_button.pack(pady=10)

image_container = tk.Canvas(window, width=900, height=600, bg="white")
image_container.pack()

window.mainloop()

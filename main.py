import tkinter as tk
from tkinter import ttk

import image_editor

window = tk.Tk()

window.title("Photo Editor")
window.geometry("1000x700")
window.config(bg="white")

tool_container = tk.Frame(window, width=1000, height=100)
tool_container.grid(row=2, column=4)
tool_container.pack(side="top", fill="x")

add_image_button = tk.Button(tool_container, command=lambda: image_editor.add_image(image_container), text="Add Image", bg="white")
add_image_button.grid(row=0, column=0, rowspan=2, padx=15, pady=5)

filter_dropdown_label = tk.Label(tool_container, text="Select Filter")
filter_dropdown_label.grid(row=0, column=1, padx=15, pady=0)

filter_values=["Black & White", "Blur", "Contour", "Detail", "Edge Enhance", "Edge Enhance More",
                "Emboss", "Find Edges", "Sharpen", "Smooth", "Smooth More"]
filter_dropdown = ttk.Combobox(tool_container, values=filter_values)
filter_dropdown.grid(row=1, column=1, padx=15, pady=(0, 5))
filter_dropdown.bind("<<ComboboxSelected>>", lambda event: image_editor.select_filter(filter_dropdown.get(), image_container))

clear_filters_button = tk.Button(tool_container, command=lambda: image_editor.clear_filters(image_container), text="Clear filters", bg="white")
clear_filters_button.grid(row=0, column=2, rowspan=2, padx=15, pady=5)

save_image_button = tk.Button(tool_container, command=image_editor.save_image, text="Save", bg="white")
save_image_button.grid(row=0, column=3, rowspan=2, padx=15, pady=5)

image_container = tk.Canvas(window, width=900, height=600, bd=0, highlightthickness=0, bg="white")
image_container.pack()

window.mainloop()

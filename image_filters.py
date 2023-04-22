from PIL import ImageOps, ImageFilter

def filter_image(filter, image):
    match filter:
        case "Black & White":
            return ImageOps.grayscale(image)
        case "Blur":
            return image.filter(ImageFilter.BLUR)
        case "Contour":
            return image.filter(ImageFilter.CONTOUR)
        case "Detail":
            return image.filter(ImageFilter.DETAIL)
        case "Edge Enhance":
            return image.filter(ImageFilter.EDGE_ENHANCE)
        case "Edge Enhance More":
            return image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        case "Emboss":
            return image.filter(ImageFilter.EMBOSS)
        case "Find Edges":
            return image.filter(ImageFilter.FIND_EDGES)
        case "Sharpen":
            return image.filter(ImageFilter.SHARPEN)
        case "Smooth":
            return image.filter(ImageFilter.SMOOTH)
        case "Smooth More":
            return image.filter(ImageFilter.SMOOTH_MORE)
        case _:
            return image

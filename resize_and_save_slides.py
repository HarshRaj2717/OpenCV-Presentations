import os
from PIL import Image


def resize_and_save_slides(slides):
    # Resize all slides to 1280x720 pixels
    # and save into the temp directory
    for slide in slides:
        original_image = Image.open(slide)
        resized_image = original_image.resize((1280, 720), Image.ANTIALIAS)
        resized_image_file_name = os.path.join(
            os.curdir, "temp", os.path.basename(slide))
        resized_image.save(resized_image_file_name)

import cv2
from PIL import Image, ImageSequence
import tempfile
import numpy as np
def resize_image(uploaded_file, sp, ext):
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as temp_file:
        source = uploaded_file.filename
        if source.lower().endswith((".jpeg", ".jpg", ".png")):
            image_data = uploaded_file.read()
            src = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_UNCHANGED)
            width = int(src.shape[1] * (100 - sp) / 100)
            height = int(src.shape[0] * (100 - sp) / 100)
            output = cv2.resize(src, (width, height))
            cv2.imwrite(temp_file.name, output)
        elif source.lower().endswith(".gif"):
            img = Image.open(uploaded_file)
            frames = []
            for frame in ImageSequence.Iterator(img):
                frame = frame.convert("RGBA")
                width, height = frame.size
                new_width = int(width * sp / 100)
                new_height = int(height * sp / 100)
                resized_frame = frame.resize((new_width, new_height), Image.ANTIALIAS)
                frames.append(resized_frame)
            frames[0].save(temp_file.name, save_all=True, append_images=frames[1:], loop=0)
    return temp_file.name
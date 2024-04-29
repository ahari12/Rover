from PIL import Image
import numpy as np
image = Image.open("red b.jpg")
image_rgb = image.convert("RGB")
image_np = np.array(image_rgb)
lower_red = np.array([150, 0, 0])
upper_red = np.array([255, 100, 100])
mask = np.all(np.logical_and(image_np >= lower_red, image_np <= upper_red), axis=-1)
masked_image_np = np.zeros_like(image_np)
masked_image_np[mask] = image_np[mask]
masked_image = Image.fromarray(masked_image_np)
bbox = masked_image.getbbox()
cropped_image = masked_image.crop(bbox)
cropped_image.save("cropped_red_object1.jpg")
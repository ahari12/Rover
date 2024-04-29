from PIL import Image
import numpy as np
 

def resize_image(image, size):
    return image.resize(size)

# Load the original and cropped images
input_image=Image.open("red b.jpg")
original_image = Image.open("testtube.jpg")
original_image1=Image.open("red b.jpg")
cropped_image = Image.open("cropped_red_object.jpg")

# Resize both images to the same dimensions (e.g., 256x256)
target_size = (256, 256)
original_resized = resize_image(original_image, target_size)
original_resized2 = resize_image(original_image1, target_size)
cropped_resized = resize_image(cropped_image, target_size)
input_image2=resize_image(input_image,target_size)
# Convert resized images to grayscale (if needed)
original_gray = original_resized.convert("L")
cropped_gray = cropped_resized.convert("L")
original_gray2=original_resized2.convert("L")
input_image=input_image2.convert("L")


# Convert images to NumPy arrays
original_np = np.array(original_gray)
cropped_np = np.array(cropped_gray)
original2_np = np.array(original_gray2)
input_np = np.array(input_image)

# Calculate MSE
mse1 = np.mean((input_np - original_np)**2)
mse2 = np.mean((input_np - cropped_np)**2)
mse3 = np.mean((input_np - original2_np)**2)
mse4 = np.mean((input_np - cropped_np)**2)
if(mse1<=10):
    angle=0
    print(angle)
elif(mse2<=10):
    print(mse2)
    angle=30
    print(angle)
elif(mse3<=10):
    angle=45
    print(angle)
elif(mse4<=10):
    angle=60
    print(angle)

# # Print the MSE value
# print("Mean Squared Error (MSE):", mse)


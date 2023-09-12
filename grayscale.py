import cv2
import os

# Specify the directory containing the images
images_dir = 'C:\\Users\\Asus\\OneDrive\\Documents\\!!!SKRIPSIJEES\\data\\tolong'

# Get the list of image file names
image_files = os.listdir(images_dir)

# Iterate over the image files
for image_file in image_files:
    # Construct the full path to the image file
    image_path = os.path.join(images_dir, image_file)

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image with a new file name
    new_file_name = 'grayscale_' + image_file
    new_image_path = os.path.join(images_dir, new_file_name)
    cv2.imwrite(new_image_path, gray_image)

print("file already grayscaled")
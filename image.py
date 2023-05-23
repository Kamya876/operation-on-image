import cv2
import numpy as np

# Read the imagepip install opencv-python


image = cv2.imread('kamya.jpg')

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Scale the image
scale_percent = 50  # Define the scale percentage
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
scaled_image = cv2.resize(image, (width, height))

# Display the scaled image
cv2.imshow('Scaled Image', scaled_image)
cv2.waitKey(0)

# Rotate the image
angle = 45  # Define the rotation angle
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

# Display the rotated image
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)

# Translate the image
translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])  # Define the translation matrix
translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))

# Display the translated image
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)

# Flip the image horizontally
flipped_image = cv2.flip(image, 1)

# Display the flipped image
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)

# Flip the image vertically
flipped_image = cv2.flip(image, 0)

# Display the flipped image
cv2.imshow('Flipped Image', flipped_image)
cv2.waitKey(0)

cv2.destroyAllWindows()

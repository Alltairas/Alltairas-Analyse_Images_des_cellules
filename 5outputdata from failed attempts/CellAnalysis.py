# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 21:45:16 2023

@author: aras
"""
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

img = Image.open(r'C:\Users\aras\Desktop\M2\ProjetAnalyseImage\noyaux\noyaux-01.png').convert('L')
img.save('greyscale_noyaux-01.png')
# Load your color image (replace 'your_color_image.jpg' with the actual image path)

# Convert the color image to grayscale
gray_image = Image.open('greyscale_noyaux-01.png')

# Define the size of the local neighborhood (mask size) and C, a constant subtracted from the mean
block_size = 101  # Adjust the block size based on your image and cell size
C = 5  # Adjust the constant C

# Define a Gaussian-weighted mask
gaussian_mask = np.outer(
    np.exp(-0.5 * np.arange(-block_size // 2, block_size // 2) ** 2 / (C ** 2)),
    np.exp(-0.5 * np.arange(-block_size // 2, block_size // 2) ** 2 / (C ** 2))
) / (2 * np.pi * C ** 2)

# Define a mean (average) mask
mean_mask = np.ones((block_size, block_size))

# Create empty output arrays for adaptive thresholding
adaptive_gaussian = np.zeros_like(gray_image)
adaptive_mean = np.zeros_like(gray_image)

# Iterate through rows and columns of the grayscale image
for y in range(gray_image.shape[0]):
    for x in range(gray_image.shape[1]):
        # Calculate local neighborhood for the current pixel
        neighborhood = gray_image[
            max(0, y - block_size // 2): min(gray_image.shape[0], y + block_size // 2 + 1),
            max(0, x - block_size // 2): min(gray_image.shape[1], x + block_size // 2 + 1)
        ]

        # Calculate the weighted average using the masks
        weighted_average_gaussian = np.sum(neighborhood * gaussian_mask)
        weighted_average_mean = np.sum(neighborhood * mean_mask)

        # Apply thresholding using the weighted averages
        adaptive_gaussian[y, x] = 255 if gray_image[y, x] > weighted_average_gaussian else 0
        adaptive_mean[y, x] = 255 if gray_image[y, x] > weighted_average_mean else 0

# Display the original grayscale image and the two thresholded images
plt.subplot(131), plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(adaptive_gaussian, cmap='gray')
plt.title('Adaptive Gaussian Thresholding'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(adaptive_mean, cmap='gray')
plt.title('Adaptive Mean Thresholding'), plt.xticks([]), plt.yticks([])

plt.show()

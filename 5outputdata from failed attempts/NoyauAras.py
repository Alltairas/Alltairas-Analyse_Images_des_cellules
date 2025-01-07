# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import numpy as np
from skimage import filters, measure
import os

# Directory containing your images
image_directory = r'D:\CellsAras'

# Create or open the text file to store results
result_file_path = 'CellCountage.txt'
with open(result_file_path, 'w') as result_file:
    result_file.write("Image Name\tCell Count\tThreshold Value\n")

    # Loop through each image in the directory
    for i in range(1, 17):
        image_name = f'noyaux-{str(i).zfill(2)}.jpg'
        image_path = os.path.join(image_directory, image_name)

        # Read the grayscale image using PIL
        image = Image.open(image_path).convert('L')

        # Convert the image to a NumPy array
        image_array = np.array(image)

        # Apply Gaussian blur to the image
        blurred_image = filters.gaussian(image_array, sigma=1.111)

        # Apply mean thresholding to create a binary image
        fixed_threshold = filters.threshold_mean(blurred_image)
        binary_image = blurred_image > fixed_threshold

        # Label connected components in the binary image
        labeled_cells = measure.label(binary_image)

        # Count the number of unique labels (cells)
        cell_count = np.max(labeled_cells)

        # Write results to the text file
        result_file.write(f"{image_name}\t{cell_count}\t{fixed_threshold}\n")

# Print a message indicating the process is complete
print("Cell counting and thresholding completed. Results saved to 'CellCountage.txt'.")

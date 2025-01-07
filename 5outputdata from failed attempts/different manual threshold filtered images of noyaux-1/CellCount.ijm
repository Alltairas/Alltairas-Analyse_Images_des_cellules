// ImageJ macro for cell counting with manual threshold, Gaussian blur, and particle analysis

// Open the image (replace "YourImagePath" with the actual path to your image)
open("C:\\Users\\aras\\Desktop\\M2\\ProjetAnalyseImage\\noyaux\\noyaux-01.png");

// Convert the image to 8-bit (if not already in 8-bit)
run("8-bit");

// Apply Gaussian blur
run("Gaussian Blur...", "sigma=2");

// Set the manual threshold to 60
setThreshold(0, 60);

// Convert the image to binary
run("Convert to Mask");

// Fill holes in the binary image
run("Fill Holes");

// Watershed segmentation (optional, may improve separation of closely spaced cells)
run("Watershed");

// Analyze particles (adjust the size and circularity as needed)
run("Analyze Particles...", "size=20-Infinity circularity=0.30-1.00 show=Overlay display exclude summarize");

// Get the number of particles (cells)
nCells = nResults;
print("Number of Cells: " + nCells);

// Check if there are results before attempting to get the count
if (nCells > 0) {
    // Display the threshold values and cell count in the Log window
    print("Manual Threshold: 60");
    print("Number of Cells: " + nCells);
} else {
    print("No particles found or an error occurred during analysis.");
}

// Save the filtered image with the original image's name as PNG
saveAs("PNG", "C:\\Users\\aras\\Desktop\\M2\\ProjetAnalyseImage\\noyaux\\noyaux-01_Filtered.png");
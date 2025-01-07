// Specify the directory path
directoryPath = "C:/Users/aras/Desktop/M2/ProjetAnalyseImage/noyaux/";

// Open the original image
open(directoryPath + "noyaux.tif");

// Duplicate the image
run("Duplicate...", "title=noyauxCopy.tif duplicate");

// Enhance Contrast
run("Enhance Contrast...", "saturated=0.35 normalize equalize");

// Make Binary
run("Make Binary", "calculate black list");

// Erode
run("Erode", "stack");

// Dilate
run("Dilate", "stack");

// Watershed
run("Watershed", "stack");

// Analyze Particles
run("Analyze Particles...", "size=0.20-Infinity circularity=0.30-1.00 show=[Bare Outlines] display exclude include summarize overlay add composite stack");
// Save the thresholdings as Text Image
selectWindow("Log");
saveAs("Text", directoryPath + "Thresholdings.txt");

// Save individual particle information
saveAs("Results", directoryPath + "IndividualParticles.csv");

// Save the drawing as Tiff
saveAs("Tiff", directoryPath + "Drawing of noyauxCopy.tif");
close();
// Close the original image
run("Close");
// Close the duplicate image
close();
# Cell Counting with an ImageJ Macro

An ImageJ/Fiji macro that counts cell nuclei, frame by frame, in a 16-frame TIFF image stack. For each
frame it also measures the average particle size and the percentage of the area they cover.

> M2 image-analysis course project — Aras Selahiye

## Pipeline

The macro (`3imj Macro/CellCount5.ijm`) works on a duplicate of the stack, so the raw data is never
modified:

1. **Enhance Contrast**: saturated 0.35 %, normalize + equalize
2. **Make Binary**: automatic threshold per slice; the thresholds are logged
3. **Erode → Dilate**: removes isolated noise pixels and small artefacts
4. **Watershed**: splits touching nuclei using a distance map from each object's centre
5. **Analyze Particles**: size ≥ 0.20, circularity 0.30–1.00, edge particles excluded

## Results

In the sample stack the count drops from about 4 000 to about 2 500 particles between frame 1 and frame 16.
Over the same frames the average particle size increases and the covered area stays roughly constant
(about 11–12 %). The full discussion is in the report.

## Repository layout

| Folder | Content |
|--------|---------|
| `1Rapport en html et ipyn/` | Project report (Jupyter notebook + HTML export) |
| `2Figures/` | Figures used in the report (processing stages, profile plots, results) |
| `3imj Macro/` | `CellCount5.ijm`, the final macro |
| `4Output Data/` | Example outputs: per-slice summary, per-particle measurements, thresholds |
| `5outputdata from failed attempts/` | Earlier approaches: manual thresholding, Gaussian blur, Sobel edge detection and adaptive thresholding in Python |

## Usage

1. Install [Fiji](https://fiji.sc/) (ImageJ with plugins).
2. Open `CellCount5.ijm` and set `directoryPath` to the folder that contains your `noyaux.tif` stack.
   You can change the file name to analyse any other stack.
3. In ImageJ: **Plugins → Macros → Run…** and select the macro.
4. The macro writes these files into the same folder:
   - `Thresholdings.txt`: threshold values used per slice
   - `IndividualParticles.csv`: measurements for each particle
   - `Drawing of noyauxCopy.tif`: outlines of the detected particles

> **Known issue:** the per-slice *Summary* table sometimes isn't saved automatically (an ImageJ
> inconsistency). If that happens, save it manually from its window.

## References

- [ImageJ Macro Language reference](https://imagej.net/ij/docs/macro_reference_guide.pdf)
- Course lectures by Hélène Delanoë-Ayari; thanks to Hugo Saint-Olive

---


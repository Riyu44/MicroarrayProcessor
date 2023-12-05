# MicroarrayProcessor
The repository contains multiple tools which can be used to aid in the field of "Digital Pathology" involving the 10x genomics software tools like SpaceRanger/Loupe Browser.

## Tools
- **AnnotateMap** - Can be used to highlight the 'fullres.jpg' image of the SpaceRanger output file and extract pixels and barcodes of the tissues using the csv files dataset.
- **Tester software** - This is the testing software for the above two tools to check if we have extracted the pixels of the image that were intended or not.

## Files
- **software.py** - The main software file to open the image, annotate (once image opens click on the area of interest and shade it) and save (click 's' to save the pixels annotated).
- **barcodes.py** - Once the pixels are saved run this file to map the corresponding barcodes
- **backtrack.py** - Use this to map the pixels saved to the image and open the modified image

## Requirements
- You need to have the 'fullres.jpg' as well as the 'tissue_positions.csv' file in the same directory as the code scripts for the code to work

## Deployment
To deploy this project you need Python3 or above and the following dependencies

```bash
  pip install opencv-python
```
```bash
  pip install matplotlib
```
```bash
  pip install numpy
```
```bash
  pip install pandas
```
```bash
  pip install Pillow
```
```bash
  pip install tkinter
```
```bash
  pip install scipy
```

## Running the scripts
- Use the below commands sequentially to annotate and extract barcode and then test it
```bash
  python software.py
```
```bash
  python barcodes.py
```
```bash
  python backtrack.py
```


## Authors

- [@Riyu44](https://www.github.com/Riyu44)

# MicroarrayProcessor
The repository contains multiple tools which can be used to aid in the field of "Digital Pathology" involving the 10x genomics software tools like SpaceRanger/Loupe Browser.

## Running Demo
**All the steps are done in itr_2 directory**
- **Step-1** 
Clone the repository and install all the requirements (see deployments section)
- **Step-2** 
Download the sample image data and save it into the 'itr_2' directory - https://www.dropbox.com/s/3iujycshhojja6q/Cn3.jpg?dl=0 
- **Step-3** 
Run the script software.py followed by barcodes.py using the commands below, where '<name of the downloaded sample image>' is 'Cn3.jpg' by default. Follow the functionalities sub-heading to get started.
```bash
  python software.py <name of the downloaded sample image>
```
```bash
  python barcodes.py
```
## Functionalities
**1. Software.py**
- Press 'f' key to use freehand draw
- Press 'c' key to toggle to circle draw
- Press 's' to save the pixels into 'contours_and_circle.csv'

**2. Barcodes.py**
- Once 'contours_and_circle.csv' is created, you can simply run the script to extract the corresponding barcodes

**The above demo and functionality corresponds to itr_2 directory. You can follow same steps with itr_1 directory only exception being the absence of circle tool in itr_1 directory**

## Tools
- **AnnotateMap** - Can be used to highlight the 'fullres.jpg' image of the SpaceRanger output file and extract pixels and barcodes of the tissues using the csv files dataset.
- **Tester software** - This is the testing software for the above two tools to check if we have extracted the pixels of the image that were intended or not.

## Files
- **software.py** - The main software file to open the image, annotate (once image opens click on the area of interest and shade it) and save (click 's' to save the pixels annotated).
- **barcodes.py** - Once the pixels are saved run this file to map the corresponding barcodes
- **backtrack.py** - Use this to map the pixels saved to the image and open the modified image
- **integration_example.R** - This contains the method to integrate the python scripts into the R environment

## Requirements
- You need to have the 'fullres.jpg' as well as the 'tissue_positions.csv' file in the same directory as the code scripts for the code to work

## Deployment
To deploy this project you need Python3 or above and the dependencies in the requrirements.txt file.

```bash
pip install -r requirements.txt
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

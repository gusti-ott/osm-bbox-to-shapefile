This small cross-language tool allows you to extract road data from OpenStreetMap for any rectangular area by specifying its bounding box. The road network is downloaded using a Python script (via the Overpass API) and saved as a shapefile, which can then be used in MATLAB or any GIS software. This is especially useful when working in MATLAB but needing precise geospatial data from OSM in a reproducible way.

# Bounding Box to OSM Shapefile (Windows)

This module downloads OpenStreetMap (OSM) road data for a given bounding box using Python and saves it as a shapefile, which can then be used in MATLAB.

...

## 1. Python Setup & Usage (Windows only)

### 1.1 Create and activate a virtual environment

Create
```bash
python -m venv venv
````

Activete in command prompt
```bash
venv\Scripts\activate
```

or 

in PowerShell
```bash
venv\Scripts\Activate.ps1
```

### 1.2 Install required Python packages

```bash
pip install osmnx
```

### 1.3 Ensure the Python script `osm_helper.py` is present

It must contain the following function:

```python
def download_osm_roads_to_shapefile(bbox, shapefile_path):
    """
    bbox: [south, west, north, east] as float values
    shapefile_path: e.g. 'roads.shp'
    """
```

This function downloads the road data and writes a shapefile with all necessary components (`.shp`, `.shx`, `.dbf`, `.prj`, etc.).

---

## 2. MATLAB Usage (Windows)

### 2.1 Set Python interpreter (only once)

You find the correct path to the virtual environment's Python Interpreter after having set up 
the virtual environment in your project folder. The path should look like this:

```
C:/FULL_PATH_TO_PYTHON_PROJECT/venv/Scripts/python.exe
```

In the **MATLAB terminal**, run:

```bash
pyenv('Version', 'C:/full/path/to/venv/Scripts/python.exe');
```

Replace the path with the actual path to your virtual environment’s Python interpreter.

### 2.2 Run the MATLAB script

In the MATLAB script `main.m`, include:

```bash
main.m
```

This will generate a shapefile with:

* `roads.shp` – geometry
* `roads.shx` – shape index
* `roads.dbf` – attribute table
* `roads.prj` – projection info

Do **not delete** any of these files. They are all required for the shapefile to function properly.

To read the shapefile in MATLAB (requires Mapping Toolbox):

```matlab
roads = shaperead('roads.shp');
```

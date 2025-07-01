% Step 1: Import OSM Helper Custom Python Module
py.importlib.import_module('osm_helper');

% Step 2: Define bounding box and output path
bbox = py.list({11.307655,44.509636,11.432625,44.579956});  % Example: Milan
output_path = 'roads.shp';

% Step 3: Call Python function
py.osm_helper.download_osm_roads_to_shapefile(bbox, output_path);

disp('Road shapefile downloaded successfully.');
import osmnx as ox


def download_osm_roads_to_shapefile(bbox, shapefile_path):
    """
    bbox: [south, west, north, east]
    shapefile_path: path to save shapefile (e.g., 'roads.shp')
    """

    # Download road network
    G = ox.graph_from_bbox(bbox, network_type='drive')

    # Convert to GeoDataFrame
    gdf = ox.graph_to_gdfs(G, nodes=False, edges=True)

    # Save to shapefile
    gdf.to_file(shapefile_path)
    return shapefile_path

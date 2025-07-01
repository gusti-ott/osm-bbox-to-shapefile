from osm_helper import download_osm_roads_to_shapefile


def main():
    path = 'roads.shp'
    bbox = [11.307655, 44.509636, 11.432625, 44.579956]  # [south, west, north, east]
    download_osm_roads_to_shapefile(bbox, path)
    print(f"OSM roads downloaded and saved to {path}")


if __name__ == "__main__":
    main()

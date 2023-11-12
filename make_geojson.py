import copy
import json
import os

import commons
import config


def make_geojson(raw_data: dict):
    # Preparing the output data structure
    print("Preparing the output GeoJSON structure...")
    geojson_data_feet = {
        "type": "FeatureCollection",
        "features": list()
    }

    # Converting to GeoJSON
    print(f"Converting to GeoJSON...")
    for raw_airport_key, raw_airport_data in raw_data.items():
        geojson_data_feet["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [raw_airport_data["lon"], raw_airport_data["lat"]]
                },
                "properties": {
                    "icao": raw_airport_data["icao"],
                    "iata": raw_airport_data["iata"],
                    "name": raw_airport_data["name"],
                    "city": raw_airport_data["city"],
                    "state": raw_airport_data["state"],
                    "elevation": raw_airport_data["elevation"],
                    "tz": raw_airport_data["tz"]
                }
            }
        )

    # Saving to output file
    print("Saving 'airports_full_all_feet.geojson'...")
    with open(os.path.join(config.OUTPUT_DIR, "airports_full_all_feet.geojson"), "w") as f:
        f.write(json.dumps(geojson_data_feet, separators=(',', ':')))

    # Preparing the meter-variant 'airports_full_all_meter'
    print("Preparing 'airports_full_all_meter.geojson'...")
    geojson_data_meters = copy.deepcopy(geojson_data_feet)
    for tmp_geo_json_airport in geojson_data_meters["features"]:
        tmp_geo_json_airport["properties"]["elevation"] = round(
            tmp_geo_json_airport["properties"]["elevation"] / 3.2808399, config.METER_DECIMAL_COUNT)
    print("Saving 'airports_full_all_meter.geojson'...")
    with open(os.path.join(config.OUTPUT_DIR, "airports_full_all_meter.geojson"), "w") as f:
        f.write(json.dumps(geojson_data_meters, separators=(',', ':')))

    # Preparing the IAIA-only variant
    # geojson_data_iata_feet = copy.deepcopy(geojson_data_feet)
    # geojson_data_iata_meter = copy.deepcopy(geojson_data_meters)


if __name__ == "__main__":
    # > Printing the logs header
    commons.print_header("GeoJSON File Maker", 5)

    # Preparing the output directory
    commons.prepare_output(config.OUTPUT_DIR)

    # Loading the JSON raw data file.
    _raw_data = commons.get_clean_data(config.INPUT_FILE)

    # Running the actual logic
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    make_geojson(_raw_data)

    # Printing the logs footer
    commons.print_footer()

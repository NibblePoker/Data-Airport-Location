import copy
import gc
import json
import os
import shutil
import sys

import config


def print_footer(message: str = "Goodbye :)", is_error: bool = False) -> None:
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    if is_error:
        print(f"\033[31m{message}\033[39m")
    else:
        print(message)
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    print(" \033[96m\\_\\ \033[36m\\_\\             \033[36m/_/ \033[96m/_/\033[39m")


if __name__ == "__main__":
    # > Printing the logs header
    print("          \033[36m_   \033[94m__  \033[36m_\033[39m")
    print("     \033[96m_  \033[36m_// \033[94m/\\\\ \\ \033[36m\\\\_  \033[96m_\033[39m")
    print("   \033[96m_// \033[36m/ / \033[94m/ /_\\ \\ \033[36m\\ \\ \033[96m\\\\_\033[39m")
    print("  \033[96m/ / \033[36m/ / \033[94m/ ___\\\\ \\ \033[36m\\ \\ \033[96m\\ \\\033[39m")
    print(" \033[96m/_/ \033[36m/_/ \033[94m/_/     \033[94m\\_\\ \033[36m\\_\\ \033[96m\\_\\\033[39m")
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    print("  \033[36mTraefik Logs Preprocessor\033[39m")
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")

    # Removing old output directory
    if os.path.exists(config.OUTPUT_DIR):
        print(f"Removing old build folder...")
        if os.path.isdir(config.OUTPUT_DIR):
            shutil.rmtree(config.OUTPUT_DIR)
        else:
            raise IOError(f"The output location '{config.OUTPUT_DIR}'is a file !")

    # Creating new output directory
    print(f"Preparing '{config.OUTPUT_DIR}'...")
    os.mkdir(config.OUTPUT_DIR)

    # Loading the JSON raw data file.
    print(f"Loading '{config.INPUT_FILE}'...")
    with open(config.INPUT_FILE, "rb") as f:
        raw_data = json.loads(f.read().decode("utf-8"))
    print(f"Loaded '{len(raw_data)}' airport(s) !")

    # Validating the data
    print(f"Validating & fixing the data...")
    was_data_valid = True
    for raw_airport_key, raw_airport_data in raw_data.items():
        for required_field in ["icao", "iata", "name", "city", "state", "country", "elevation", "lat", "lon", "tz"]:
            if not (required_field in raw_airport_data):
                print(f"ERROR: Airport '{raw_airport_key}' is missing the '{required_field}' field !")
                was_data_valid = False
            if type(raw_airport_data[required_field]) is str:
                if len(raw_airport_data[required_field]) == 0:
                    raw_airport_data[required_field] = None
        if raw_airport_data["icao"] is None and raw_airport_data["iata"] is None:
            print(f"ERROR: Airport '{raw_airport_key}' is missing its ICAO and IATA codes !")
            was_data_valid = False
        if raw_airport_data["name"] is None:
            print(f"ERROR: Airport '{raw_airport_key}' is missing its name !")
            was_data_valid = False
        if raw_airport_data["country"] is None:
            print(f"ERROR: Airport '{raw_airport_key}' is missing its country code !")
            was_data_valid = False
    if not was_data_valid:
        print_footer("Cannot continue, we have invalid data !", True)
        sys.exit(1)

    # Preparing the output data structure
    print(f"Preparing the output structure...")
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

    # Printing the logs footer
    print_footer()

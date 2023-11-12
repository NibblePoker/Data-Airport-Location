import copy
import gc
import json
import os

import commons
import config

import simplekml


def make_kml(raw_data: dict):
    # Preparing the output data structure
    print("Preparing the output KML structure...")
    kml_main = simplekml.Kml()

    # Converting to KML
    print(f"Converting data to KML points...")
    for raw_airport_key, raw_airport_data in raw_data.items():
        pnt = kml_main.newpoint(
            name=f"{raw_airport_data['icao']} - {raw_airport_data['name']}",
            coords=[(raw_airport_data['lon'], raw_airport_data['lat'], )],
        )
        pnt.name = raw_airport_key
        pass

    print("Saving 'airports_full.kml'...")
    kml_main.save(os.path.join(config.OUTPUT_DIR, "airports_full.kml"))

    # Helping the GC along
    del kml_main
    gc.collect()


if __name__ == "__main__":
    # > Printing the logs header
    commons.print_header("KML File Maker", 7)

    # Preparing the output directory
    commons.prepare_output(config.OUTPUT_DIR)

    # Loading the JSON raw data file.
    _raw_data = commons.get_clean_data(config.INPUT_FILE)

    # Running the actual logic
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    make_kml(_raw_data)

    # Printing the logs footer
    commons.print_footer()

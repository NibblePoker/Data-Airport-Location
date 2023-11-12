import commons
import config

from make_geojson import make_geojson
from make_kml import make_kml


if __name__ == "__main__":
    # > Printing the logs header
    commons.print_header("Data File Maker", 7)

    # Preparing the output directory
    commons.prepare_output(config.OUTPUT_DIR)

    # Loading the JSON raw data file.
    _raw_data = commons.get_clean_data(config.INPUT_FILE)

    # Running the actual logic
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    make_geojson(_raw_data)
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    make_kml(_raw_data)

    # Printing the logs footer
    commons.print_footer()

import json
import os
import shutil
import sys


# Data adapted from ISO 3166-1
# Source: https://en.m.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)
COUNTRY_IN_CONTINENT = {
    # Africa
    "AF": ["AO", "BF", "BI", "BJ", "BW", "CD", "CF", "CG", "CI", "CM", "CV", "DJ", "DZ", "EG", "EH", "ER", "ET", "GA",
           "GH", "GM", "GN", "GQ", "GW", "IO", "KE", "KM", "LR", "LS", "LY", "MA", "MG", "ML", "MR", "MU", "MW", "MZ",
           "NA", "NE", "NG", "RE", "RW", "SC", "SD", "SH", "SL", "SN", "SO", "SS", "ST", "SZ", "TD", "TF", "TG", "TN",
           "TZ", "UG", "YT", "ZA", "ZM", "ZW"],

    # Antarctica
    "AN": ["AQ", "BV", "GS", "HM"],

    # Asia
    "AS": ["AE", "AF", "AM", "AZ", "BD", "BH", "BN", "BT", "CC", "CN", "CX", "CY", "EG", "GE", "HK", "ID", "IL", "IN",
           "IQ", "IR", "JO", "JP", "KG", "KH", "KP", "KR", "KW", "KZ", "LA", "LB", "LK", "MM", "MN", "MO", "MV", "MY",
           "NP", "OM", "PH", "PK", "PS", "QA", "RU", "SA", "SG", "SY", "TH", "TJ", "TL", "TM", "TR", "TW", "UZ", "VN",
           "XD", "XS", "YE"],

    # Europe
    "EU": ["AD", "AL", "AM", "AT", "AX", "AZ", "BA", "BE", "BG", "BY", "CH", "CY", "CZ", "DE", "DK", "EE", "ES", "FI",
           "FO", "FR", "GB", "GE", "GG", "GI", "GR", "HR", "HU", "IE", "IM", "IS", "IT", "JE", "KZ", "LI", "LT", "LU",
           "LV", "MC", "MD", "ME", "MK", "MT", "NL", "NO", "PL", "PT", "RO", "RS", "RU", "SE", "SI", "SJ", "SK", "SM",
           "TR", "UA", "VA", "XK"],

    # North America
    "NA": ["AG", "AI", "AW", "BB", "BL", "BM", "BQ", "BS", "BZ", "CA", "CR", "CU", "CW", "DM", "DO", "GD", "GL", "GP",
           "GT", "HN", "HT", "JM", "KN", "KY", "LC", "MF", "MQ", "MS", "MX", "NI", "PA", "PM", "PR", "SV", "SX", "TC",
           "TT", "UM", "US", "VC", "VG", "VI"],

    # Oceania
    "OC": ["AS", "AU", "CK", "FJ", "FM", "GU", "KI", "MH", "MP", "NC", "NF", "NR", "NU", "NZ", "PF", "PG", "PN", "PW",
           "SB", "TK", "TO", "TV", "UM", "VU", "WF", "WS", "XX"],

    # South America
    "SA": ["AR", "BO", "BR", "CL", "CO", "EC", "FK", "GF", "GY", "PE", "PY", "SR", "UY", "VE"]
}


def prepare_output(output_path: str) -> None:
    # Removing old output directory
    if os.path.exists(output_path):
        print(f"Removing old build folder...")
        if os.path.isdir(output_path):
            shutil.rmtree(output_path)
        else:
            raise IOError(f"The output location '{output_path}'is a file !")

    # Creating new output directory
    print(f"Preparing '{output_path}'...")
    os.mkdir(output_path)


def get_clean_data(input_file: str) -> dict:
    print(f"Loading '{input_file}'...")
    with open(input_file, "rb") as f:
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

    return raw_data


def print_header(app_name: str, space_count: int = 0) -> None:
    print("          \033[36m_   \033[94m__  \033[36m_\033[39m")
    print("     \033[96m_  \033[36m_// \033[94m/\\\\ \\ \033[36m\\\\_  \033[96m_\033[39m")
    print("   \033[96m_// \033[36m/ / \033[94m/ /_\\ \\ \033[36m\\ \\ \033[96m\\\\_\033[39m")
    print("  \033[96m/ / \033[36m/ / \033[94m/ ___\\\\ \\ \033[36m\\ \\ \033[96m\\ \\\033[39m")
    print(" \033[96m/_/ \033[36m/_/ \033[94m/_/     \033[94m\\_\\ \033[36m\\_\\ \033[96m\\_\\\033[39m")
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    print(f"{' '*space_count}\033[36m{app_name}\033[39m")
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")


def print_footer(message: str = "Goodbye :)", is_error: bool = False) -> None:
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    if is_error:
        print(f"\033[31m{message}\033[39m")
    else:
        print(message)
    print("\033[36m-\033[94m===========================\033[36m-\033[39m")
    print(" \033[96m\\_\\ \033[36m\\_\\             \033[36m/_/ \033[96m/_/\033[39m")

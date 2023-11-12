# Directory where all files will be saved to.
OUTPUT_DIR = "./output"

# Input file path from "mwgg/Airports".
INPUT_FILE = "./data/mwgg/Airports/airports.json"

# Number of decimal places in meter elevations
METER_DECIMAL_COUNT = 0

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

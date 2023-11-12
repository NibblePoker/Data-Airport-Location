import json
import config


if __name__ == "__main__":
    with open(config.INPUT_FILE, "rb") as f:
        raw_data = json.loads(f.read().decode("utf-8"))

    country_codes = list()

    for raw_airport_key, raw_airport_data in raw_data.items():
        if raw_airport_data["country"] is None:
            continue
        if len(raw_airport_data["country"]) == 0:
            continue
        if not (raw_airport_data["country"] in country_codes):
            country_codes.append(raw_airport_data["country"])

    country_codes.sort()

    print(",".join(country_codes))

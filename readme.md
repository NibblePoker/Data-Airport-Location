# GeoJSON & KML Airport Data
GeoJSON & KML sets of 28k+ airports with ICAO/IATA codes, names, cities, two-letter country identifiers,
elevation, latitude & longitude, and a timezone identifier.

**This repo is entirely based on data provided by [mwgg/Airports](https://github.com/mwgg/Airports) !**

## Downloading
If you just want to download the files, just head over to the
[release page](https://github.com/NibblePoker/Data-Airport-Location/releases).

## Running
If you want to run this script yourself, you simply need to run the following commands:
```shell
git clone --recurse-submodules https://github.com/NibblePoker/Data-Airport-Location.git
cd Data-Airport-Location
pip install -r requirements.txt
python make_all.py
```
Your newly baked GeoJSON files should be in the `output/` folder.

## GeoJSON Structure
All `.geojson` files use the following standard structure:
```json
{
  "type":"FeatureCollection",
  "features":[
    {
      "type":"Feature",
      "geometry":{
        "type":"Point",
        "coordinates":[-151.695999146,59.94919968]  // As [longitude,latitude]
      },
      "properties":{
        "icao":"00AK",
        "iata":null,
        "name":"Lowell Field",
        "city":"Anchor Point",
        "state":"Alaska",
        "elevation":450,  // Can be in feet or meters.
        "tz":"America/Anchorage"
      }
    }
    // More may follow here.
  ]
}
```

## Remarks
All future continent-based filtering will be done using 
[Wikipedia's list](https://en.m.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file))
that is itself based on `ISO 3166-1`.

## License
The datasets provided by this repository is based on the dataset provided by
[mwgg/Airports](https://github.com/mwgg/Airports) and is licensed under the
[MIT License](https://github.com/mwgg/Airports/blob/master/LICENSE).

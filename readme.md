# GeoJSON Airport Data
GeoJSON sets of 28k+ airports with ICAO/IATA codes, names, cities, two-letter country identifiers, elevation, latitude & longitude, and a timezone identifier.

**This repo is entirely based on data provided by [mwgg/Airports](https://github.com/mwgg/Airports) !**

## Structure

### GeoJSON
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
All continent-based filtering is done using 
[Wikipedia's list](https://en.m.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file))
that is itself based on `ISO 3166-1`.

## License
The datasets provided by this repository is based on the dataset provided by
[mwgg/Airports](https://github.com/mwgg/Airports) and is licensed under the
[MIT License](https://github.com/mwgg/Airports/blob/master/LICENSE).

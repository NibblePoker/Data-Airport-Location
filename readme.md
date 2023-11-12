# Airport Location Data

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

## Notes
https://en.m.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)


## License
The datasets provided by this repository is based on the dataset provided by
[mwgg/Airports](https://github.com/mwgg/Airports) and is licensed under the
[MIT License](https://github.com/mwgg/Airports/blob/master/LICENSE).

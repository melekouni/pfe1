window.onload = init ;
function init(){
    


    const mapElement = document.getElementById('mapid')
     var map = L.map(mapElement).setView([37.232263, 9.988891], 10);
     L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        attribution: 'malik'
    }).addTo(map);





    // FeatureGroup is to store editable layers
    var drawnItems = new L.FeatureGroup();
    map.addLayer(drawnItems);
    var drawEditControl = new L.Control.Draw({
        draw: false,
        edit: {
            featureGroup: drawnItems
        }
    });
    var drawControl = new L.Control.Draw({
        draw: {
            circle:false,
            rectangle:false,
            polyline:false,
            circlemarker:false,
            marker:false,
            polygon: {
                icon: new L.DivIcon({
                    iconSize: new L.Point(10, 10),
                    className: 'leaflet-div-icon leaflet-editing-icon'
                }),
                shapeOptions: { color: 'red', opacity: 0.3, fillOpacity: 0.5, weight: 10 },
                showArea: true,
            }
          }
        });      
  
    
    map.addControl(drawControl);

    
  
    map.on('draw:created', function (e) {
        var type = e.layerType;
        layer = e.layer;
        
        if (type === 'polygon'){
            drawnItems.addLayer(layer);
            // console.log("coord : "+e.layer.toGeoJSON().geometry.coordinates);
            myjson=drawnItems.toGeoJSON() ;
        }
        
        let coords = [];
        myjson.features.forEach((coordonne) => {
            coords.push(coordonne.geometry)
        });
        console.log(coords);
            // const multiPolygone = { 
            //     "type": "MultiPolygon",
            //     "coordinates": [
            //         [...coords]
            //     ]
            // }
            // console.log(multiPolygone)
        document.getElementById('cord').value=JSON.stringify(coords);
     });
   


    

    map.on('draw:edited', function (e) {
        layer = e.layers;
        console.log(layer)
        const coordinates = layer._layers[Object.keys(layer._layers)[0]]._latlngs[0];
        let polygon = [];
        coordinates.forEach((element) => {
            polygon.push(`${element.lng} ${element.lat}`);
        });
        polygon.push(`${coordinates[0].lng} ${coordinates[0].lat}`);
        polygonString = 'POLYGON (('+polygon.join(', ')+'))';
        document.getElementById('cord').value=polygonString;
    });

    map.on('draw:deleted', function () {
        drawControl.addTo(map);
        drawEditControl.remove();
        document.getElementById('cord').value='';
    });
  
}
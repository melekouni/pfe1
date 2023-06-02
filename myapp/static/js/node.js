window.onload = init ;
function init(){
    
    var coordinates= document.getElementById('polygone').value;
    console.log(coordinates)
    coordinates = coordinates.replace(/'/gm,'"');
    var coordinatesJson = JSON.parse(coordinates);  
    
    var points= document.getElementById('nodes').value;
   
    console.log(points)
    points = points.replace(/'/gm,'"');
    var pointsJson = JSON.parse(points);
    console.log(pointsJson)
    
    const mapElement = document.getElementById('idmap')
    var map = L.map(mapElement).setView([37.232263, 9.988891], 10);
    L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
       attribution: 'malik map'
   }).addTo(map);
   L.geoJSON(coordinatesJson,{color : 'blue',opacity: 0.3, fillOpacity: 0.5, weight: 10 }).addTo(map)
   L.geoJSON(pointsJson).addTo(map)
    //  coordinatesJson.forEach(({ fields }) => {
    
    //   L.geoJSON(geos,{color : 'blue',opacity: 0.3, fillOpacity: 0.5, weight: 10 }).addTo(map)
//   })


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
            marker:true  ,
            polygon:false,
           
        },
    });
    map.addControl(drawControl);

    
  
    map.on('draw:created', function (e) {
        layer = e.layer;
        const coordinates = layer.toGeoJSON();
        document.getElementById('points').value=JSON.stringify(coordinates.geometry);
        drawnItems.addLayer(layer);
        drawControl.remove();
        drawEditControl.addTo(map);
    });
 
    map.on('draw:edited', function (e) {
        layer = e.layers;
        const coordinates = layer.toGeoJSON();
        console.log(coordinates);
        document.getElementById('points').value=JSON.stringify(coordinates.features[0].geometry);
      
    });

    map.on('draw:deleted', function () {
        drawControl.addTo(map);
        drawEditControl.remove();
        document.getElementById('points').value='';
    });
  
}

window.onload = init ;
function init(){
    var coordinates= document.getElementById('points').value;
    console.log()
    coordinates = coordinates.replace(/'/gm,'"');
    var coordinatesJson = JSON.parse(coordinates);
    console.log(coordinatesJson)

    var points= document.getElementById('point').value;
    console.log(points)
    points = points.replace(/'/gm,'"');
    var pointsJson = JSON.parse(points);
    console.log(pointsJson[0])
    var  p=  pointsJson[0].coordinates
    var x=p[1] 
    var y=p[0] 
    var pl = document.getElementById('pol').value;
    console.log(pl)
    const mapElement = document.getElementById('map')
    var map = L.map(mapElement).setView([x, y], 11);
    L.tileLayer('http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
       attribution: ''
   }).addTo(map);
   var idn= document.getElementById('idn').value;
   console.log(idn)
    
   L.geoJSON(coordinatesJson,{color : 'blue',opacity: 0.2, fillOpacity: 0.3, weight: 15 }).addTo(map)
   
   L.geoJSON(pointsJson).addTo(map).bindPopup(idn)




}
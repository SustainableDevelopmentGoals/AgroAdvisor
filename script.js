var map = new ol.Map({
      target: 'map',
      layers: [
        new ol.layer.Tile({
          source: new ol.source.OSM()
        })
      ],
      view: new ol.View({
        center: ol.proj.fromLonLat([38.85, 8.98]),
        zoom: 12
      })
    });
var layer = new ol.layer.Vector({
   source: new ol.source.Vector({
   }),
   style: new ol.style.Style( {
        image: new ol.style.Circle( {
            radius: 5,
            text: "test",
            fill: new ol.style.Fill( {
                color: '#2e279d'
            } )
        } ) })
 });
var old = new ol.layer.Vector({
  source: new ol.source.Vector({
  })
})
map.addLayer(layer)
map.addLayer(old)
var current_items = []
map.on('singleclick', function (event) {
   var lonlat = ol.proj.transform(event.coordinate, 'EPSG:3857', 'EPSG:4326');
   console.log(lonlat)
   layer.getSource().clear()
   layer.getSource().addFeature(
      new ol.Feature({
            geometry: new ol.geom.Point(ol.proj.fromLonLat([lonlat[0],lonlat[1]]))
      })
    )
   $("#lon_val").text(lonlat[0])
   $("#lat_val").text(lonlat[1])
   $("#add_registration").prop("disabled",false)
   // console.log(map.getLayers())
});

$("#send_advice").click(function() {
    $.ajax({
    method: "GET",
    url: "http://127.0.0.1:5000/advice",
    contentType: "application/json"
  })
    .done(function( msg ) {
      object = JSON.parse(msg)
      for(var i=0; i<object.length; i++){
          weather = object[i].weather_info
          advice_string = object[i].advice
          //console.log(weather)
          console.log(advice_string)
      }
  });
})

$("#add_registration").click(function() {
  var name = $("#name").val()
  var lat = parseFloat($("#lat_val").text())
  var lon = parseFloat($("#lon_val").text())
  json = {name:name,lat:lat,lon:lon}
  $.ajax({
    method: "POST",
    url: "http://127.0.0.1:5000/register",
    data:JSON.stringify(json),
    contentType: "application/json"
  })
    .done(function( msg ) {
      console.log("OK")
      get_registrations()
  });
})

function get_registrations() {
   $.ajax({
    method: "GET",
    url: "http://127.0.0.1:5000/registrations",
    contentType: "application/json"
  })
    .done(function( data ) {
          $(".registration").remove()
          data = JSON.parse(data)
          current_items = data
          for (var i=0; i<data.length;i++){
             handle_registration(data[i])
          }
      })
}

function handle_registration(data) {
    console.log(data)
    var registration = $("<div/>", {
        'class':'registration'
    })
//    var general_info = $("<div/>", {
//        'class':'info_pane'
//    })
//    var labels = $("<div/>", {
//        'class':'labels'
//    })
    var name_div = $("<div>",{
        'class':'name_div'
    })
    var name_label = $("<h4>",{
        text: "Name"
    })
    var name = $("<p>",{
        text: data.name
    })
    name_div.append(name_label)
    name_div.append(name)
//    var lat = $("<p>",{
//        text: data.info.lat
//    })
//    var lon = $("<p>",{
//        text: data.info.lon
//    })
     var rain_div = $("<div>",{
        'class':'rain_div'
    })
    var rain_label = $("<h4>",{
        text: "Total rainfall"
    })
    var rainfall = $("<p>",{
        text: data.weather_advice.weather_info.total_rainfall
    })
    rain_div.append(rain_label)
    rain_div.append(rainfall)
    var wind_div = $("<div>",{
        'class':'wind_div'
    })
    var wind_label = $("<h4>",{
        text: "Max wind speed"
    })
    var wind = $("<p>",{
        text: data.weather_advice.weather_info.max_wind_speed
    })
    wind_div.append(wind_label)
    wind_div.append(wind)

    var temp_div = $("<div>",{
        'class':'temp_div'
    })
    var temp_label = $("<h4>",{
        text: "Avg day temp"
    })
    var temp = $("<p>",{
        text: data.weather_advice.weather_info.avg_temperature_day
    })
    temp_div.append(temp_label)
    temp_div.append(temp)

    var advice_div = $("<div>",{
        'class':'name_div',
        'style':'width:130px;float:left;'
    })
    var advice_label = $("<h4>",{
        text: "Advice"
    })
    var advice = $("<p>",{
        text: data.weather_advice.advice,
        'style':'font-size:10px'
    })
    advice_div.append(advice_label)
    advice_div.append(advice)
//    var switch_button = $('<button/>', {
//        text: "View current weather and advice",
//        'class': 'switch_button',
//        click: handle_click
//    });
   // general_info.append(name)
//    general_info.append(lat)
//    general_info.append(lon)
//    general_info.append(name)
//    general_info.append(rainfall)
//    general_info.append(wind)
//    general_info.append(temp)
//    general_info.append(advice)
    registration.append(name_div)
    registration.append(rain_div)
    registration.append(wind_div)
    registration.append(temp_div)
    registration.append(advice_div)
    //registration.append(switch_button)
    $("#registrations").append(registration)

}

//function handle_click() {
//    var info = $(this).parent().find(".info_pane")
//    var advice = $(this).parent().find(".weather_advice")
//    if(info.css("display") === 'block') {
//        info.css("display","none")
//        advice.css("display","inline-flex")
//    } else {
//        info.css("display","inline-flex")
//        advice.css("display","none")
//    }
//}

$(get_registrations)

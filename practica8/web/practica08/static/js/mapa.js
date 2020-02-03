var map;
var madrid = { lat: 40.4381311, lng: -3.8196195 };
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: madrid,
    zoom: 5
  });

  var marker = new google.maps.Marker({
    map: map,
    position: madrid,
    title: "click para cerrar"
  });
  marker.addListener("click", () => marker.setVisible(false));
}

$("#geolocalizacion").click(function(e) {
  e.preventDefault();
  var infoWindow = new google.maps.InfoWindow();

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      position => {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };

        map.setZoom(8);
        infoWindow.setPosition(pos);
        infoWindow.setContent("Usted está aquí");
        infoWindow.open(map);
        map.setCenter(pos);
      },
      () => handleLocationError(true, infoWindow, map.getCenter())
    );
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }

  function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(
      browserHasGeolocation
        ? "Error: The Geolocation service failed."
        : "Error: Your browser doesn't support geolocation."
    );
    infoWindow.open(map);
  }
});

$("#posicion").click(function(e) {
  e.preventDefault();
  $.ajax({
    type: "get",
    url: "/p6/get_posicion_musicos",
    dataType: "json",
    success: function(response) {
      for (var pos in response) {
        var marker = new google.maps.Marker({
          map: map,
          // Las latitudes y las longitudes están invertidas porque las puse al revés al copiarla
          // en los modelos
          position: {lat: response[pos]['lon'], lng: response[pos]['lat']},
          title: response[pos]['nombre']
        });
      }
      map.setZoom(5)
      map.setCenter(madrid)
    }
  });
});

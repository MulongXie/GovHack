function addMarker(loc, map, data) {
    // Add the marker at the clicked location, and add the next-available label
    // from the array of alphabetical characters.
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(loc[0], loc[1]),
        label: data,
        map: map
    });
    markers.push(marker);
}

function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

function markerList() {
    clearMarkers();
    for (var i in cdlist) {
        var loc = cdlist[i];
        addMarker(loc, globelMap, "60");
    }
}

function clearMarkers() {
    setMapOnAll(null);
}
var input = document.getElementById("location");
var options = {
  types: ["geocode"],
};
var autocomplete = new google.maps.places.Autocomplete(input, options);

autocomplete.addListener("place_changed", function () {
  var place = autocomplete.getPlace();
  var locationInput = document.getElementById("location");
  locationInput.value = place.formatted_address;
});

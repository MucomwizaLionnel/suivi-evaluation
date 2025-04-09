<script>
document.addEventListener("DOMContentLoaded", function () {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            document.getElementById("id_latitude").value = position.coords.latitude;
            document.getElementById("id_longitude").value = position.coords.longitude;
        }, function (error) {
            console.error("Erreur de géolocalisation :", error);
        })
    } else {
        console.error("Géolocalisation non supportée par ce navigateur.")
    }
});
</script>

<div id="map" style="height: 300px;"></div>

<script>
document.addEventListener("DOMContentLoaded", function () {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;

            document.getElementById("id_latitude").value = latitude;
            document.getElementById("id_longitude").value = longitude;

            var map = L.map('map').setView([latitude, longitude], 13);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; OpenStreetMap contributors'
            }).addTo(map);

            L.marker([latitude, longitude]).addTo(map)
                .bindPopup("Vous êtes ici")
                .openPopup();
        }, function (error) {
            console.error("Erreur de géolocalisation :", error);
        });
    }
});
</script>

<!-- Ajoute ce lien dans le <head> de ton HTML -->
<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>


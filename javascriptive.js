<script>
document.addEventListener("DOMContentLoaded", function () {
    if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(function (position) {
            document.getElementById("id_latitude").value = position.coords.latitude;
            document.getElementById("id_longitude").value = position.coords.longitude;
        }, function (error) {
            console.error("Erreur de géolocalisation :", error);
        });
    } else {
        console.error("Géolocalisation non supportée par ce navigateur.");
    }
});
</script>

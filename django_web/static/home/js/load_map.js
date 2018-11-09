let map = L.map('map').setView([35.696849, 105.732332], 4);
let basemap = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let province_border_shp = $.ajax({
    // url: "./dis_dashboard/ProvinceBorder/?format=json&reg_id=0",
    url: "./dis_dashboard/ProvinceBorder/?format=json&reg_id_not=0",
    dataType: "json",
    success: function () {
        console.log("ProvinceBorder data successfully loaded.");
        // console.log(province_border_shp);
    },
    error: function (xhr) {
        alert(xhr.statusText)
        // alert(province_border_shp)
    }
});

$.when(province_border_shp).done(function () {
    let province_border_geoJSON = L.geoJSON(province_border_shp.responseJSON.results, {
            style: function (feature) {
                return {
                    fillColor: 'red',
                    "fillOpacity": 0
                }
            },

            onEachFeature: function (feature, layer) {
                layer.bindPopup(feature.properties.name.toString());
            }
        }
    ).addTo(map);

})

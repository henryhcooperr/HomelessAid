document.addEventListener('DOMContentLoaded', function() {
    console.log('Document loaded, initializing maps...');
    document.querySelectorAll('.resource-item').forEach((resource) => {
        const addressElement = resource.querySelector('p:nth-child(2)'); // More specific selector
        const address = addressElement.innerText.replace('Address: ', '').trim();
        const mapDiv = resource.querySelector('.map');
        console.log(`Initializing map for address: ${address} with element ID: ${mapDiv.id}`);
        initMap(mapDiv.id, address);
    });
});

function initMap(elementId, address) {
    console.log(`Calling geocoder for address: ${address}`);
    const geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'address': address }, function(results, status) {
        console.log(`Geocode status for ${address}: ${status}`);
        if (status === 'OK') {
            console.log(`Result for ${address}:`, results[0].geometry.location);
            const map = new google.maps.Map(document.getElementById(elementId), {
                center: results[0].geometry.location,
                zoom: 14,
            });
            new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
        } else {
            console.error('Geocode was not successful for the following reason: ' + status);
        }
    });
}

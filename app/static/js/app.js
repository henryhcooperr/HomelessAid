document.getElementById('search-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form from submitting the traditional way
    document.getElementById('loading').style.display = 'block'; // Show the loader

    // Example of hiding the loader when done (adjust based on actual use)
    setTimeout(() => {
        document.getElementById('loading').style.display = 'none'; // Hide the loader after a delay
        // You should replace this with actual AJAX call and response handling
    }, 3000); // Simulate delay for demonstration
});

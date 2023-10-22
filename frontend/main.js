function fetchDataFromBackend() {
    fetch('http://localhost:8080/')
        .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Do something with the data received from the backend
        console.log(data);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

  // Call the function initially
fetchDataFromBackend();
const intervalId = setInterval(fetchDataFromBackend, 5000);
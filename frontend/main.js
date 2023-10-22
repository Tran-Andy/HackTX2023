function fetchDataFromBackend() {
    fetch('http://localhost:8080/',{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body: JSON.stringify({'id':'bruh'})
    });

}

  // Call the function initially
fetchDataFromBackend();
const intervalId = setInterval(fetchDataFromBackend, 5000);
const form = document.querySelector('form');  
const cityInput = document.querySelector('#city');  
const weatherDataDiv = document.querySelector('#weather-data');  

form.addEventListener('submit', (e) => {  
    e.preventDefault();  // Prevent the default form submission behavior
    const city = cityInput.value.trim();  // Get the city input value

    if (city) {  
        fetch(`/weather?city=${encodeURIComponent(city)}`)  // Fetch weather data
            .then((response) => {
                if (!response.ok) {  // Check if the response is successful
                    throw new Error('City not found');  // Throw an error if city is not found
                }
                return response.json();  // Parse the JSON response
            })
            .then((data) => {  
                // Create HTML to display weather data
                const weatherDataHtml = `
                    <h2>Weather in ${city}</h2>
                    <p>Temperature: ${data.temp}°C</p>  
                    <p>Feels like: ${data.feels_like}°C</p>  
                    <p>Main: ${data.main}</p>  
                    <p>Updated at: ${data.dt}</p>  
                `;  
                weatherDataDiv.innerHTML = weatherDataHtml;  // Update the weather data div
            })  
            .catch((error) => {  
                weatherDataDiv.innerHTML = `<p>Error: ${error.message}</p>`;  // Display error message
                console.error(error);  // Log error to the console
            });  
    } else {
        weatherDataDiv.innerHTML = '<p>Please enter a city.</p>';  // Prompt user to enter a city if input is empty
    }  
});

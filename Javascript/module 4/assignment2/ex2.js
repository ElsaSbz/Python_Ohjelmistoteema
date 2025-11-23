//Develop the app further.
// Add JavaScript that gets the value entered to the form and sends a request with fetch to https://api.tvmaze.com/search/shows?q=${value_from_input}. Print the search result to the console. (3p)

document.getElementById("searchForm").addEventListener("submit", function(event) {
            event.preventDefault();
            const query = document.getElementById("query").value;
            const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;
            fetch(apiUrl)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    console.log(data);
                    if (data.length > 0) {
                        data.forEach(show => {
                            console.log(`Show: ${show.show.name}, Premiered: ${show.show.premiered}`);
                        });
                    } else {
                        console.log("No results found.");
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        });
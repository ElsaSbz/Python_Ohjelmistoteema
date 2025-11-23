//Make an app that retrieves information about a TV series you enter and displays it in the console. (2p)
// API to use: TVMaze API
// First, make a valid HTML page with a search form. Example form:
// <form action="https://api.tvmaze.com/search/shows">
//   <input id="query" name="q" type="text">
//   <input type="submit" value="Search">
// </form>
// Test the form. The result should be a page full of JSON formatted data.

document.getElementById("searchForm").addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent the default form submission

            const query = document.getElementById("query").value;
            const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

            fetch(apiUrl)
                .then(response => response.json())
                .then(data => {
                    console.log(data); // Log the JSON data to the console
                })
                .catch(error => {
                    console.error('Error fetching data:', error); // Log any errors
                });
        });
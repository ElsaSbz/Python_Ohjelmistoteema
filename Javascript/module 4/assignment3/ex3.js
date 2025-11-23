//Develop the app even further. Print the following information for all series from the search result on the web page. (7p)
// required information: Name, link to details (url), medium image and summary
// show the name in <h2> element
// show the url in <a> element. Also add target="_blank" to the link.
// show the medium image with <img src="" alt="">. Add medium image to src attribute and name property to alt attribute.
// some TV-shows don't have images. This will cause an error. You can fix this by adding ? operator to image property. Example: tvShow.show.image?.medium;. This is called optional chaining.
// show summary in <div> element (not <p>). This is because the summary is already in <p> element, and the result will not be valid if <p> is inside another <p>.
// collect the elements to <article> elements and append <article> elements to the HTML document.
// make <div id="results"> element to the HTML document where you append the <article> elements.
// clear the old results with innerHTML = '' before you append the new results.

document.getElementById("searchForm").addEventListener("submit", function(event) {
            event.preventDefault();
            const query = document.getElementById("query").value;
            const apiUrl = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;
            document.getElementById("results").innerHTML = '';

            fetch(apiUrl)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.length > 0) {
                        data.forEach(tvShow => {
                            const article = document.createElement('article');

                            const h2 = document.createElement('h2');
                            h2.textContent = tvShow.show.name;
                            article.appendChild(h2);

                            const link = document.createElement('a');
                            link.href = tvShow.show.url;
                            link.target = "_blank";
                            link.textContent = "See Details";
                            article.appendChild(link);

                            const img = document.createElement('img');
                            img.src = tvShow.show.image?.medium || '';
                            img.alt = tvShow.show.name;
                            article.appendChild(img);

                            const summary = document.createElement('div');
                            summary.innerHTML = tvShow.show.summary;
                            article.appendChild(summary);

                            document.getElementById("results").appendChild(article);
                        });
                    } else {
                        const noResults = document.createElement('div');
                        noResults.textContent = "No results found.";
                        document.getElementById("results").appendChild(noResults);
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                });
        });
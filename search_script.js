
let articles = [];

 // Fetch articles from JSON
fetch('https://poonh.github.io/travel_blog/articles.json')
  .then(response => {
    console.log('Fetched articles.json:', response);
    return response.json();
  })
  .then(data => {
    console.log('Loaded articles:', data);
    articles = data;
  })
  .catch(error => console.error('Error fetching articles.json:', error));


// Search function
function searchArticles() {
  const query = document.getElementById("search-box").value.toLowerCase().trim();

  // Split query into individual keywords by spaces
  const keywords = query.split(/\s+/);

  const resultsContainer = document.getElementById("search-results");
  resultsContainer.innerHTML = ""; // Clear previous results

  if (keywords.length > 0) {
    const filteredArticles = articles.filter(article => {
      // Check if ALL keywords match ANY property of the article
      return keywords.every(keyword =>
        article.title.toLowerCase().includes(keyword) ||
        article.description.toLowerCase().includes(keyword) ||
        article.tags.some(tag => tag.toLowerCase().includes(keyword))
      );
    });

    // Display results
    if (filteredArticles.length > 0) {
      // Store search results in sessionStorage (this is temporary data for the session)
      sessionStorage.setItem('searchResults', JSON.stringify(filteredArticles));

      // Open a new tab with the search results
      window.open('search_results.html', '_blank');
    } else {
      alert('没有结果');
    }
  }
}

// Mobile search function
function searchMobileArticles() {
  const query = document.getElementById("search-mobile-box").value.toLowerCase().trim();

  // Split query into individual keywords by spaces
  const keywords = query.split(/\s+/);

  const resultsContainer = document.getElementById("search-results");
  resultsContainer.innerHTML = ""; // Clear previous results

  if (keywords.length > 0) {
    const filteredArticles = articles.filter(article => {
      // Check if ALL keywords match ANY property of the article
      return keywords.every(keyword =>
        article.title.toLowerCase().includes(keyword) ||
        article.description.toLowerCase().includes(keyword) ||
        article.tags.some(tag => tag.toLowerCase().includes(keyword))
      );
    });

    // Display results
    if (filteredArticles.length > 0) {
      // Store search results in sessionStorage (this is temporary data for the session)
      sessionStorage.setItem('searchResults', JSON.stringify(filteredArticles));

      // Open a new tab with the search results
      window.open('search_results.html', '_blank');
    } else {
      alert('没有结果');
    }
  }
}

// Add event listener to the "Search" button
document.getElementById("search-button").addEventListener("click", searchArticles);
document.getElementById("search-box").addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    searchArticles();
  }
});


document.getElementById("search-mobile-button").addEventListener("click", searchMobileArticles);
document.getElementById("search-mobile-box").addEventListener("keypress", (event) => {
  if (event.key === "Enter") {
    searchMobileArticles();
  }
});

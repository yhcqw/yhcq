import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Base URL to scrape
base_url = "https://poonh.github.io/grandparents/index.html"

# Destination folder to save the HTML files
folder_path = os.path.expanduser("~/Desktop/yhcq2")

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Fetch the HTML content of the main page
response = requests.get(base_url)
response.raise_for_status()

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract all anchor tags with href attributes
links = soup.find_all("a", href=True)

# Loop through each link
for link in links:
    href = link['href']
    
    # Construct the full URL from the base URL
    full_url = urljoin(base_url, href)


    # Only proceed if the URL is under the same site
    if urlparse(full_url).netloc == urlparse(base_url).netloc:
        try:
            # Fetch the HTML content of the link
            link_response = requests.get(full_url)
            link_response.raise_for_status()

            # Generate a valid filename from the URL path
            filename = os.path.basename(urlparse(full_url).path) or "index.html"
            file_path = os.path.join(folder_path, filename)

            # Save the HTML content to a file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(link_response.text)
            
            print(f"Saved {full_url} to {file_path}")
        except requests.RequestException as e:
            print(f"Failed to fetch {full_url}: {e}")

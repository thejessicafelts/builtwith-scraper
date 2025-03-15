import requests
from bs4 import BeautifulSoup

# Define the base URL.
base_url = "http://builtwith.com/"

# Read endpoints from a separate file (each endpoint on a new line).
with open("endpoints.txt", "r", encoding="utf-8") as f:
    endpoints = [line.strip() for line in f if line.strip()]

# Create the full URL list.
websites = [base_url + endpoint for endpoint in endpoints]

# Use a set to store unique technology names.
unique_technologies = set()

for url in websites:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    # Extract technology texts from the specified selector.
    anchor_elements = soup.select(".container .row .col-md-8 .card .card-body .row .col-12 h2 a")
    
    for a in anchor_elements:
        tech = a.get_text(strip=True)
        unique_technologies.add(tech)

# Optionally sort the list.
unique_technologies_list = sorted(unique_technologies)

# Write the unique technologies to the output file.
with open("output.txt", "w", encoding="utf-8") as file:
    for tech in unique_technologies_list:
        file.write(f"{tech}\n")
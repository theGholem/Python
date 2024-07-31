import requests
from bs4 import BeautifulSoup

def get_website_info(url):
    try:
        # Send an HTTP request to get the content of the web page
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the title of the page
        title = soup.title.string if soup.title else 'No title found'

        # Extract the description of the page (meta description tag)
        description = ''
        if soup.find('meta', attrs={'name': 'description'}):
            description = soup.find('meta', attrs={'name': 'description'}).get('content')

        # Extract other public information (meta keywords tag)
        keywords = ''
        if soup.find('meta', attrs={'name': 'keywords'}):
            keywords = soup.find('meta', attrs={'name': 'keywords'}).get('content')

        # Display the extracted information
        info = {
            'title': title,
            'description': description,
            'keywords': keywords
        }

        return info

    except requests.exceptions.RequestException as e:
        return f"Error fetching the website: {e}"

# Prompt the user to enter the target website URL
url = input("Please enter the target website URL: ")
website_info = get_website_info(url)
print(website_info)

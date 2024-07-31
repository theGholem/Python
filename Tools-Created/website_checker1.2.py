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

        # Extract headings
        headings = [heading.text.strip() for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]

        # Extract links
        links = [link.get('href') for link in soup.find_all('a', href=True)]

        # Extract images
        images = [img.get('src') for img in soup.find_all('img', src=True)]

        # Extract social media links (basic example)
        social_media_links = []
        for link in links:
            if 'facebook.com' in link or 'twitter.com' in link or 'linkedin.com' in link or 'instagram.com' in link:
                social_media_links.append(link)

        # Display the extracted information
        info = {
            'title': title,
            'description': description,
            'keywords': keywords,
            'headings': headings,
            'links': links,
            'images': images,
            'social_media_links': social_media_links
        }

        return info

    except requests.exceptions.RequestException as e:
        return f"Error fetching the website: {e}"

# Prompt the user to enter the target website URL
url = input("Please enter the target website URL: ")
website_info = get_website_info(url)
print(website_info)

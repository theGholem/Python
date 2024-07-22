import requests
from bs4 import BeautifulSoup

def check_twitter(username):
    twitter_url = f"https://twitter.com/{username}"
    response = requests.get(twitter_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_name = soup.find('a', class_='ProfileHeaderCard-nameLink u-textInheritColor js-nav')
        if profile_name:
            return twitter_url
    return None

def check_instagram(username):
    instagram_url = f"https://www.instagram.com/{username}"
    response = requests.get(instagram_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        meta = soup.find('meta', property='og:description')
        if meta and f'@{username}' in meta.get('content'):
            return instagram_url
    return None

def check_facebook(username):
    facebook_url = f"https://www.facebook.com/{username}"
    response = requests.get(facebook_url)
    if response.status_code == 200:
        return facebook_url
    return None

def check_linkedin(username):
    linkedin_url = f"https://www.linkedin.com/in/{username}"
    response = requests.get(linkedin_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        profile_name = soup.find('h1', class_='top-card-layout__title')
        if profile_name and username.lower() in profile_name.text.lower():
            return linkedin_url
    return None

def find_social_accounts(username):
    social_accounts = {}

    twitter_account = check_twitter(username)
    if twitter_account:
        social_accounts['Twitter'] = twitter_account

    instagram_account = check_instagram(username)
    if instagram_account:
        social_accounts['Instagram'] = instagram_account

    facebook_account = check_facebook(username)
    if facebook_account:
        social_accounts['Facebook'] = facebook_account

    linkedin_account = check_linkedin(username)
    if linkedin_account:
        social_accounts['LinkedIn'] = linkedin_account

    return social_accounts

if __name__ == "__main__":
    username = input("Entrez le nom d'utilisateur pour rechercher les comptes sociaux : ")

    accounts = find_social_accounts(username)

    if accounts:
        print(f"Comptes sociaux trouvés pour '{username}':")
        for platform, url in accounts.items():
            print(f"{platform}: {url}")
    else:
        print(f"Aucun compte social trouvé pour '{username}'. Vérifiez l'exactitude du nom d'utilisateur.")


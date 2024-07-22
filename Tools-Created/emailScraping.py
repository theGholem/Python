from bs4 import BeautifulSoup
import requests
import urllib.parse
from collections import deque
import re

# Entrée de l'utilisateur
user_url = str(input('[+] Entrez L\'URL Cible à Scanner: '))
urls = deque([user_url])

# Ensembles pour les URLs et les emails
urls_scraped = set()
emails = set()

# Compteur de pages traitées
compteur = 0

try:
    while len(urls):
        compteur += 1
        if compteur == 100:
            break

        url = urls.popleft()
        urls_scraped.add(url)

        parties = urllib.parse.urlsplit(url)
        url_de_base = '{0.scheme}://{0.netloc}'.format(parties)
        path = url[:url.rfind('/')+1] if '/' in parties.path else url

        print('[%d] Traitement %s' % (compteur, url))
        try:
            response = requests.get(url)
            response.encoding = 'utf-8'  # S'assurer que l'encodage est en UTF-8
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        nouveaux_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
        emails.update(nouveaux_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):
            lien = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if lien.startswith('/'):
                lien = url_de_base + lien
            elif not lien.startswith('http'):
                lien = path + lien
            if lien not in urls and lien not in urls_scraped:
                urls.append(lien)
except KeyboardInterrupt:
    print('[-] Fermeture!')

for mail in emails:
    print(mail)

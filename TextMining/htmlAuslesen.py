'''
Created on 26 Apr 2020

@author: Daten Master
'''

#####################################################################################################################
# Bibliotheken importieren
#####################################################################################################################
import requests
from bs4 import BeautifulSoup

#####################################################################################################################
# Inhalte der Webseite abrufen
#####################################################################################################################
URL = 'https://www.enzyklopaedie-der-wirtschaftsinformatik.de/lexikon/technologien-methoden/text-mining'
page = requests.get(URL)

#####################################################################################################################
# Inhalte der Webseite mit BeautifulSoup verwalten
#####################################################################################################################
soup = BeautifulSoup(page.content, 'html.parser')

#####################################################################################################################
# Bestimmtes Element der Webseite auslesen
#####################################################################################################################
results = soup.find(id='content')

#####################################################################################################################
# ausgelesene Texte wiedergeben
#####################################################################################################################
#print(results)
#print(results.text)

# Titel
print(results.text[15:27])

# Was ist Text Mining?
print(results.text[131:344])

# Ziel von Text Mining
print(results.text[356:1077])

# Vergleich Text Mining vs. Data Mining
print(results.text[1077:1564])

# Text Mining Prozess
print(results.text[1564:1738])
print(results.text[1738:1757])
print(results.text[1757:1776])
print(results.text[1776:1796])
print(results.text[1796:1818])
print(results.text[1818:1845])
print(results.text[1845:1854])
print(results.text[1854:3955])

# Anwendungsbereiche von Text Mining
print(results.text[3955:4433])

# Literatur
print(results.text[4433:4983])

# Autor
print(results.text[4992:4998])
print(results.text[5002:5164])

from bs4 import BeautifulSoup
import requests
import re 

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def fetch_results(search_term, number_results, language_code):
    assert isinstance(search_term, str), 'Search term must be a string'
    assert isinstance(number_results, int), 'Number of results must be an integer'
    escaped_search_term = search_term.replace(' ', '+')
    google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
    response = requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()

    return search_term, response.text

#test
keyword, html = fetch_results('Vintage hiking shoes men', 100, 'en')

soup = BeautifulSoup(html, 'html.parser')

#prettifying content
print(soup.prettify())

link_s = []
for bar in soup.findAll("a", attrs={'href': re.compile("^htt")}):
    bar.get("href")
    link_s.append(bar.get("href"))

for link in link_s:
    print(link)








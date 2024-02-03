import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
def Scraper():
    USER_AGENT = 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    cnt = session.get("https://mkp.gem.gov.in/search").text
    return cnt


def home(request):
    print("Initialising...")
    prod = []
    res = Scraper()
    soup = BeautifulSoup(res, 'html.parser')
    for sup in soup.find_all('li', {'class': 'bn-group'}):
        itms = []
        for itm in sup.find_all('li', {'class': 'bn-link'}):
            print(itm)
            itms.append(f"{itm.findChild()}")
        prod.append({
            'Name': f"{sup.findChild('strong').text}",
            'Cnts': itms
        })
    print(itms)
    print(prod)

    return render(request, "Home.html", {'Prods': prod})

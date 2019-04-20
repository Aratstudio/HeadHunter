import requests
# from bs4 import BeutifulSoup as bs
from urllib3 import*
from urllib.request import urlopen

headers  = {"accept":"*/*",
           "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
base_url = "https://krasnoyarsk.hh.ru/search/vacancy?area=54&clusters=true&enable_snippets=true&text=python&page=0"

def hh_parse(base_url, headers):
    session = requests.Session()
    request = session.get(base_url, headers = headers)

    if request.status_code == 200:
        print("ok")
        content = urlopen("https://www.quora.com/")
        #page=urlopen("https://krasnoyarsk.hh.ru/search/vacancy?area=54&clusters=true&enable_snippets=true&text=python&page=0")
        content.read



        # soup = bs(requests.content, "html.parser")
        #divs = soup.find_all("div", attrs = {"" : ""})
        # for div in divs:
        #               title = div.find("", attrs = {"":""}).text
        #                    href = div.find("", attrs = {"":""})[""]
        #                       company = div.find("", attrs = {"":""})

    else:
       print("ERROR")

hh_parse(base_url, headers)


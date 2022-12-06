# Web Scarper using api
import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".sitestr")
votes = soup.select(".score")


def create_custom_hn(links, votes):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get("href", None)
        hn.append({"title": title, "href": href})
    return hn


new_hn = create_custom_hn(links, votes)
print(new_hn)

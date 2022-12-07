# Web Scarper using api
import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/news")

soup = BeautifulSoup(res.text, "html.parser")
links = soup.select(".sitestr")
subtext = soup.select(".subtext")


def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        vote = subtext[i].select(".score")
        href = links[i].get("href", None)
        if len(vote):
            hn.append(
                {"title": title, "score": vote[0].getText(), "href": href})
        else:
            hn.append({"title": title, "score": None, "href": href})
    return hn


new_hn = create_custom_hn(links, subtext)
print(new_hn)

import requests
from bs4 import BeautifulSoup
from lxml import etree

response = requests.get("https://scipost.org/atom/publications/comp-ai")
xml_data = response.content
soup = BeautifulSoup(xml_data, "xml")
entries = soup.find_all("entry")

news = []
for entry in entries:
    title = entry.find("title").text
    link = entry.find("link", {"rel": "alternate"})["href"]
    summary = entry.find("summary").text if entry.find("summary") else "No summary available"

    news.append({
        "Title": title,
        "Link": link,
        "Summary": summary
    })

for n in news:
    print(f"Title: {n['Title']}")
    print(f"Link: {n['Link']}")
    print(f"Summary: {n['Summary']}")
    print("-" * 50)


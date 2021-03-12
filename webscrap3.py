import requests
from bs4 import BeautifulSoup


with requests.Session() as session:
    #session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"}
    r = session.get("https://www.zomato.com/brewbot")
    soup = BeautifulSoup(r.content, "html.parser")
    itemid = soup.body["itemid"]

    # get reviews
    r = session.post("https://www.zomato.com/php/social_load_more.php", data={
        "entity_id": itemid,
        "profile_action": "reviews-top",
        "page": "0",
        "limit": "5"
    })
    reviews = r.json()["html"]

    soup = BeautifulSoup(reviews, "html.parser")
    k_data = soup.select("div.rev-text")

    for item in k_data:
        print(item.get_text())
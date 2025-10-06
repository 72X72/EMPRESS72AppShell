import requests, json, time
from bs4 import BeautifulSoup

URL = "https://app.freecash.com/earn"
HEADERS = {
    "User-Agent": "EMPRESS72-Sovereign-Scraper",
    "Accept": "text/html"
}

def scrape_offers():
    print("[EMPRESS72] Scanning Freecash terrain...")
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    offers = []
    for div in soup.find_all("div", class_="offer-card"):
        title = div.find("h3")
        payout = div.find("span", class_="payout")
        if title and payout:
            offer = {
                "title": title.text.strip(),
                "payout": payout.text.strip(),
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            offers.append(offer)

    return offers

def log_offers(offers, log_file="earnings.log"):
    with open(log_file, "a") as f:
        for offer in offers:
            line = f"[{offer['timestamp']}] {offer['title']} → {offer['payout']}\n"
            f.write(line)
    print(f"[EMPRESS72] Logged {len(offers)} offers to {log_file}")

if __name__ == "__main__":
    offers = scrape_offers()
    if offers:
        log_offers(offers)
    else:
        print("[EMPRESS72] No offers found. Terrain may be cloaked.")

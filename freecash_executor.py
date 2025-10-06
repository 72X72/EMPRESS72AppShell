from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def launch_empress_browser():
    print("[EMPRESS72] Launching headless browser...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1280,720")

    driver = # webdriver.Chrome(options=chrome_options)
    driver.get("https://app.freecash.com/earn")
    time.sleep(5)  # Wait for JS to render

    return driver

def extract_offers(driver):
    print("[EMPRESS72] Extracting bounty terrain...")
    offers = []
    cards = driver.find_elements(By.CLASS_NAME, "offer-card")
    for card in cards:
        try:
            title = card.find_element(By.TAG_NAME, "h3").text.strip()
            payout = card.find_element(By.CLASS_NAME, "payout").text.strip()
            offers.append(f"{title} → {payout}")
        except:
            continue
    return offers

def log_offers(offers, log_file="earnings.log"):
    with open(log_file, "a") as f:
        for offer in offers:
            line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {offer}\n"
            f.write(line)
    print(f"[EMPRESS72] Logged {len(offers)} offers to {log_file}")

if __name__ == "__main__":
    driver = launch_empress_browser()
    offers = extract_offers(driver)
    driver.quit()

    if offers:
        log_offers(offers)
    else:
        print("[EMPRESS72] No bounty offers found. Terrain may be encrypted.")

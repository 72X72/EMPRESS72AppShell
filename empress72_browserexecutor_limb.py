from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def automate_browser_task(url):
    print("[EMPRESS72] 🧠 Executing browser automation")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("/data/data/com.termux/files/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        start_button = driver.find_element(By.ID, "startSurvey")
        start_button.click()
        print("[EMPRESS72] ✅ Survey started")
    except:
        print("[EMPRESS72] ⚠️ DOM element not found")

    driver.quit()

import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

# --------- DRIVER SETUP ---------
def make_driver():
    options = Options()
    options.page_load_strategy = "eager"
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=options)

# --------- REGEX HELPER ---------
def extract(pattern, text):
    m = re.search(pattern, text)
    return m.group(1).strip() if m else ""

# --------- SCRAPER ---------
def scrape_category(category):
    url = f"https://mm2values.com/?p={category}"
    print(f"\nLoading {url}")

    driver = make_driver()
    driver.set_page_load_timeout(90)

    try:
        driver.get(url)
        time.sleep(4)  # wait for JS content
    except TimeoutException:
        print("Page load timeout")
        driver.quit()
        return []

    html = driver.page_source
    driver.quit()  # CLOSE DRIVER EARLY

    soup = BeautifulSoup(html, "html.parser")
    items = []

    for block in soup.find_all("div"):
        text = block.get_text("\n", strip=True)
        if "Value:" not in text:
            continue

        lines = text.splitlines()
        name = lines[0]

        # --- FIXED: Allow decimals in rarity ---
        value = extract(r"Value:\s*([\d,]+|N/A)", text).replace(",", "")
        range_ = extract(r"Range:\s*(.+)", text)
        demand = extract(r"Demand:\s*([\d.]+)", text)
        rarity = extract(r"Rarity:\s*([\d.]+)", text)  # <-- FIXED
        stability = extract(r"Stability:\s*(.+)", text)

        items.append({
            "name": name,
            "value": value,
            "range": range_ or "N/A",
            "demand": demand or "N/A",
            "rarity": rarity or "N/A",
            "stability": stability or "N/A"
        })

    return items

# --------- MAIN LOOP ---------
categories = ["chroma"]

for cat in categories:
    data = scrape_category(cat)

    # DELETE first 3 items (usually headers)
    data = data[3:]

    filename = f"mm2values_{cat}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(f"Name: {item['name']}\n")
            f.write(f"Value: {item['value']}\n")
            f.write(f"Range: {item['range']}\n")
            f.write(f"Demand: {item['demand']}\n")
            f.write(f"Rarity: {item['rarity']}\n")
            f.write(f"Stability: {item['stability']}\n")
            f.write("-" * 40 + "\n")  # separator between items

    print(f"Saved {len(data)} items (skipped headers) -> {filename}")

print("\nDone.")

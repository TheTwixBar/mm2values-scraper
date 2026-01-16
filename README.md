**MM2Values Scraper**
A Python web scraper that uses Selenium and BeautifulSoup to extract item values from mm2values.com and save them into structured text files. This scraper is designed to work on a JavaScript-heavy site using headless Chrome.

Features:
-Scrapes MM2 item data including name, value, range, demand, rarity (decimal-safe), and stability
-Uses headless Chrome (no visible browser window)
-Automatic ChromeDriver management
-Skips header and duplicate blocks
-Outputs clean text files per category

Tech Stack:
-Python 3.9 or higher
-Selenium
-BeautifulSoup4
-webdriver-manager
-Google Chrome

Installation:
  Clone the repository:
  git clone https://github.com/TheTwixBar/mm2values-scraper.git
  cd mm2values-scraper

Install dependencies:
pip install -r requirements.txt

Ensure Google Chrome is installed:
chrome --version

Usage:
Run the scraper:
python scraper.py

After running, output files such as mm2values_chroma.txt will appear in the project directory.

Configuration

To change categories, edit the categories list in scraper.py:

categories = ["chroma"]

Example:
categories = ["chroma", "godly", "ancient"]
  If items are missing or the page loads slowly, increase the delay:
  time.sleep(4)

Example:
time.sleep(6)

Common Issues:

pip is not recognized
Python is not added to PATH. Reinstall Python and enable “Add Python to PATH”.

ChromeDriver errors
Ensure webdriver-manager is installed. It automatically matches your Chrome version.

Script runs but no data is saved
Increase the page load delay, confirm Chrome is installed, or note that the site may temporarily block automation.

Deployment Notes

This scraper works on local machines, VPS environments, and platforms like Render or Railway (Chrome must be installed). Headless mode is enabled by default.

Disclaimer:

**This project is for educational and personal use only. Always respect website terms of service and scraping policies.**

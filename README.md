 🛠️ OLX Car Cover Scraper

A Python script to scrape search results for "car cover" listings from [OLX India](https://www.olx.in/).  
It scrolls through the page, extracts item titles and links, and saves them to a `.txt` file.

---
 🔍 What It Does

- Launches a headless Chrome browser using Selenium.
- Loads OLX search results for "car cover".
- Scrolls slowly to ensure full content loading.
- Extracts:
  - ✅ Title of each listing
  - ✅ Link to the listing
- Saves the results in `olx_car_covers.txt`.

---

💻 Setup

 1. Clone the repo

git clone https://github.com/yourusername/olx-scraper.git
cd olx-scraper


### 2. Install dependencies

Make sure you have Python 3.7+ installed.


pip install selenium


### 3. Download & set up ChromeDriver

* Match the version with your Chrome browser from: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
* Add it to your system PATH or place it in the same directory as the script.

---

## 🚀 Usage

python olx_scraper.py


This will create or overwrite the file `olx_car_covers.txt` with the scraped items.

---

## 📁 Output Format

Each line in the output file will contain:


Car seat cover vsp - https://www.olx.in/item/spare-parts-...


---

## 🧠 Notes

* OLX uses dynamic content; this scraper scrolls slowly to ensure all listings load.
* If OLX changes their HTML structure, you’ll need to update the class names accordingly.

---



import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import random

def slow_scroll(driver, steps=10, pause=2):
    """Scrolls the page in gradual steps."""
    for i in range(steps):
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight * {i / steps});")
        time.sleep(pause + random.uniform(0.3, 0.7))


options = uc.ChromeOptions()
options.add_argument("--start-maximized")
driver = uc.Chrome(options=options)


url = "https://www.olx.in/items/q-car-cover"
driver.get(url)


slow_scroll(driver, steps=12, pause=2)


items = driver.find_elements(By.CSS_SELECTOR, 'li[data-aut-id="itemBox3"]')
print(f"Found {len(items)} items on the page")

results = []

for item in items:
    try:
        
        title_elem = item.find_element(By.CSS_SELECTOR, 'span._2poNJ') 

        link_elem = item.find_element(By.CSS_SELECTOR, 'a._2cbZ2') 
        
        title = title_elem.text
        link = "/"+ link_elem.get_attribute("href")  

    
       
        results.append(f"{title}\n{link}")
        
    except Exception as e:
        print(f"Error processing item: {e}")
        continue


with open("olx_car_covers.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(results))

print(f"✅ Saved {len(results)} items to olx_car_covers.txt")


driver.quit()

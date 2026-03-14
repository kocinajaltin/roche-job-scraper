from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# ---------- SETUP ----------
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless=new")  # optional


# ---------- SCRAPER FUNCTION ----------
def roche_scrape(keyword, country):

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    title_list = []
    location_list = []
    description_list = []
    url_list = []

    initial_url = f"https://careers.roche.com/global/en/search-results?keywords={keyword}"
    driver.get(initial_url)

    try:
        cookie_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Accept')]"))
        )
        cookie_button.click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 4);")
        time.sleep(2)

        loc_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Location')]"))
        )
        loc_btn.click()

        country_checkbox = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//input[@data-ph-at-text='{country}']/..")
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            country_checkbox
        )

        time.sleep(1)
        country_checkbox.click()
        time.sleep(5)

        print(f"Filtering for {country}")

    except Exception as e:
        print("Filter error:", e)

    page = 0

    while page < 60:

        print(f"{country} | {keyword} | Page index: {page}")

        if page > 0:
            url = f"{initial_url}&from={page}&s=1&location={country}"
            driver.get(url)
            time.sleep(5)

        try:

            wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li.jobs-list-item"))
            )

            jobs = driver.find_elements(By.CSS_SELECTOR, "li.jobs-list-item a")

            for job in jobs:

                try:

                    title = job.text
                    link = job.get_attribute("href")

                    try:
                        location = job.find_element(
                            By.XPATH, "../span[@class='job-location']"
                        ).text
                    except:
                        location = "N/A"

                    # ---------- OPEN JOB IN NEW TAB ----------
                    driver.execute_script(f"window.open('{link}','_blank');")
                    driver.switch_to.window(driver.window_handles[1])

                    time.sleep(2)

                    try:
                        description = wait.until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, "div.job-description, div.ph-richtext")
                            )
                        ).text
                    except:
                        description = ""

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

                    title_list.append(title)
                    location_list.append(location)
                    description_list.append(description)
                    url_list.append(link)

                except Exception as e:
                    print("Job extraction error:", e)

            page += 10

        except Exception as e:
            print("Page error:", e)
            break

    driver.quit()

    return pd.DataFrame({
        "title": title_list,
        "location": location_list,
        "description": description_list,
        "url": url_list
    })



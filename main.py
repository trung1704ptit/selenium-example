import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = 'c:/WebDrivers/chromedriver.exe'
HOMEPAGE = "https://finance.yahoo.com/quote/AAPL/profile?p=AAPL"


def get_data(url, categories):
    browser_options = ChromeOptions()
    browser_options.headless = True

    driver = Chrome(executable_path=CHROME_DRIVER_PATH, options=browser_options)



    driver.get(HOMEPAGE)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'mrt-node-Col1-0-Profile'))
        )

        # print(element.text)
        container = element.find_elements(By.CLASS_NAME, 'asset-profile-container')[0]
        com_name = container.find_elements(By.TAG_NAME, 'h3')[0].text
        p = container.find_elements(By.TAG_NAME, 'p')[0].text

        print(com_name)
        print(p.split('\n'))

    finally:
        driver.quit()


def export_csv(data):
    df = pd.DataFrame(data)
    # Apply transformations if needed
    df.to_csv("books_exported.csv", index=False)
    print(df)  # DEBUG


def main():
    get_data(url=HOMEPAGE, categories=["Humor", "Art"])
    # export_csv(data)
    # print('DONE')


if __name__ == '__main__':
    main()
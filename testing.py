from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import time

def test_app(url):
    # Setup Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Setup Chrome driver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(2)  # Wait for the page to load

        # Check if the welcome message is displayed
        welcome_message = driver.find_element(By.XPATH, "//p[contains(text(),'Welcome to PHP')]")
        assert 'Welcome to PHP' in welcome_message.text

        # Check if the table is displayed
        table = driver.find_element(By.XPATH, "//table")
        assert table.is_displayed()

        # Check if the table has the expected data
        rows = table.find_elements(By.XPATH, ".//tr")
        assert len(rows) > 1  # Ensure there is at least one data row

        # Check for specific content in the table
        first_row_data = rows[1].find_elements(By.XPATH, ".//td")
        assert len(first_row_data) == 3  
        assert first_row_data[0].text.isdigit()  
        assert first_row_data[1].text == "SampleName1" 
        assert first_row_data[2].text == "SampleValue1" 
    
        print("Test passed: Application is up and running, and the database content is correct.")
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python testing.py <url>")
        sys.exit(1)

    test_url = sys.argv[1]
    test_app(test_url)

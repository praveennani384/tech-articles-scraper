from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os
import csv  # Import the csv module

# Set up the WebDriver (using current working directory)
driver = webdriver.Chrome()

# Step 1: Open the main page (index.html)
current_directory = os.getcwd()  # Get the current working directory
url = f'file:///{current_directory}/HTML_templates/indexes/index.html'  # Construct the file URL
driver.get(url)
driver.maximize_window()
time.sleep(3)  # Wait for the page to load

# Total number of pages (you can adjust this based on your setup)
total_pages = 3

# Create or open a CSV file to write data
with open('articles_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    # Create a CSV writer object
    writer = csv.writer(csv_file)
    # Write the header row
    writer.writerow(['Title', 'Author', 'Date', 'Summary', 'Tags', 'Contact'])

    # Step 2: Loop through pages
    for page in range(total_pages):
        print(f"\nScraping Page {page + 1}...\n")

        # Locate all article links on the current page
        articles = driver.find_elements(By.XPATH, '//article/h2/a')

        for i, article_link in enumerate(articles):
            # Open each article in a new tab
            ActionChains(driver).key_down(Keys.CONTROL).click(article_link).key_up(Keys.CONTROL).perform()

            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)  # Wait for the new tab to load

            # Collect information
            title = driver.find_element(By.TAG_NAME, 'h2').text

            try:
                author = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//p[strong[text()="Author:"]]'))
                ).text.split(': ')[1]

                date = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//p[strong[text()="Date:"]]'))
                ).text.split(': ')[1]

                # Handle optional summary (it may not exist in some articles)
                try:
                    summary = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'full-content'))
                    ).text
                except TimeoutException:
                    print(f"Summary not found for article {i + 1} on page {page + 1}.")
                    summary = "No summary available"

                tags = driver.find_element(By.XPATH, '//p[strong[text()="Tags:"]]')\
                    .text.split(': ')[1]

                contact = driver.find_element(By.CLASS_NAME, 'contact')\
                    .text.split(': ')[1]

                # Print collected information
                print(f"Title: {title}")
                print(f"Author: {author}")
                print(f"Date: {date}")
                print(f"Summary: {summary}")
                print(f"Tags: {tags}")
                print(f"Contact: {contact}")
                print("-" * 40)

                # Write the data to the CSV file
                writer.writerow([title, author, date, summary, tags, contact])
            
            except TimeoutException:
                print(f"Timeout while trying to access elements for article {i + 1} on page {page + 1}.")
                print(driver.page_source)

            # Close the article tab and switch back to the main page
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)  # Short wait before processing the next article

            # Scroll down after every two articles
            if (i + 1) % 2 == 0:  # Scroll after every two articles
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)  # Wait for the scroll to complete

        # Step 3: Click on the "Next Page" link
        if page < total_pages - 1:  # Avoid clicking next on the last page
            next_page_link = driver.find_element(By.XPATH, '//div[@class="pagination"]/a')
            next_page_link.click()
            time.sleep(3)  # Wait for the next page to load

# Close the WebDriver
driver.quit()

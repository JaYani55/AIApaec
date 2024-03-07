import os
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome()
# Initialize the Chrome WebDriver
# driver = webdriver.Chrome(executable_path="C:\\Users\\Janal\\Downloads\\chromedriver_win32\\chromedriver.exe")
# Open the webpage
driver.get("https://schwarzesbrett.bremen.de/verkauf-angebote/rubrik/arbeitsplatzangebote-verkauf.html")
elements = driver.find_elements("xpath", '//*[@id="eintraege"]//a')
data = []

    # Iterate over the rows in pairs (job title, date, URL)
for element in elements:
        job_title = element.text.split('\n')[0]
        date = element.text.split('\n')[1] if '\n' in element.text else None
        url = element.get_attribute('href')
        data.append([job_title, date, url])
# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Job Title', 'Date', 'URL'])
print(df)
file_path = os.path.join('Data', 'Crawlers', 'CrawlerOutput', 'SchwBrtt_HB.csv')
os.makedirs(os.path.dirname(file_path), exist_ok=True)
df.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")
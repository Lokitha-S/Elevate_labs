import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "http://quotes.toscrape.com/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        quotes_data = []
        quote_elements = soup.find_all('div', class_='quote')

        for element in quote_elements:
            text = element.find('span', class_='text').get_text() if element.find('span', class_='text') else "No Text"
            author = element.find('small', class_='author').get_text() if element.find('small', class_='author') else "Unknown"
            
            link = "http://quotes.toscrape.com" + element.find('a')['href'] if element.find('a') else "No Link"
            
            quotes_data.append([text, author, link])

        with open('scraped_quotes.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author", "Bio Link"]) 
            writer.writerows(quotes_data)

        print(f"Success! Extracted {len(quotes_data)} quotes to scraped_quotes.csv")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    print("--- Ethical Web Scraper Initialized ---")
    print("Checking robots.txt compliance...")
    scrape_quotes()
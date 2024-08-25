import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    product_name = soup.find('h2', class_='product-name').text.strip()
    product_price = float(soup.find('span', class_='price').text.replace('$', '').strip())
    image_url = soup.find('img', class_='product-image')['src']
    
    return {
        "product_title": product_name,
        "product_price": product_price,
        "path_to_image": download_image(image_url),  
    }

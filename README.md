This application is based on Python and FastAPI for website scrapping (initially for this website: https://dentalstall.com/shop/)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. Scrape the product name, price, and image from each page of the catalogue (it’s not necessary to open each product card).
Different settings can be provided as input, so your tool should be able to recognize them and work accordingly. For the current task, you can implement only two optional settings:
    - The first one will limit the number of pages from which we need to scrape the information (for example, `5` means that we want to scrape only products from the first 5 pages).
    - The secod one will provide a proxy string that tool can use for scraping
      
2. Store the scraped information in a database. For simplicity, you can store it on your PC's local storage as a JSON file in the following format:

            [
            {
            "product_title":"",
            "product_price":0,
            "path_to_image":"", # path to image at your PC
            }
            ]

However, be aware that there should be an easy way to use another storage strategy.

3. At the end of the scraping cycle, you need to notify designated recipients about the scraping status - send a simple message that will state how many products were scraped and
   updated in DB during the current session. For simplicity, you can just print this info in the console. However, be aware that there should be an easy way to use another notification
   strategy.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
First we need to install these python packages: fastapi, uvicorn, beautifulsoup4, requests, redis

We have following files:
main.py: This file sets up the FastAPI application and defines the main routes.
scraping.py: Contains the logic for scraping product details from the website.
database.py: Handles saving and loading data to/from a local JSON file.
notification.py: Manages sending notifications about the scraping status.
authentication.py: Provides simple token-based authentication.
caching.py: Integrates Redis for caching scraping results.

Command to run the application: uvicorn main:app --reload

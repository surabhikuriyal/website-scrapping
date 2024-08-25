
from fastapi import FastAPI, Depends, HTTPException, Header
from scraping import scrape_product
from database import save_data, load_data
from notification import notify_scraping_status
from authentication import authenticate
from caching import get_cached_product, cache_product

app = FastAPI()

@app.post("/scrape/")
async def scrape(settings: dict, token: str = Depends(authenticate)):
    products = []
    for i in range(1, settings["max_pages"] + 1):
        url = f"https://dentalstall.com/shop/page/{i}"
        product_info = scrape_product(url)
        product_id = hash(product_info['product_title'])
        
        cached_product = get_cached_product(str(product_id))
        if cached_product:
            continue
        
        products.append(product_info)
        cache_product(str(product_id), product_info)
    
    save_data(products)
    notify_scraping_status(len(products))
    return {"message": "Scraping completed successfully."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

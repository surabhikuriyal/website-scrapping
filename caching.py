import redis

cache = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_product(product_id):
    return cache.get(product_id)

def cache_product(product_id, product_info):
    cache.set(product_id, json.dumps(product_info))

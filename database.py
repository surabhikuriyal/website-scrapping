import json

def save_data(data, filename='products.json'):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename='products.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

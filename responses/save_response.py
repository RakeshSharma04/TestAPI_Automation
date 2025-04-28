import json
import os

def save_response_to_file(response, filename):
    os.makedirs('responses', exist_ok=True)
    filepath = os.path.join('responses', filename)
    with open(filepath, 'w') as f:
        json.dump(response.json(), f, indent=4)

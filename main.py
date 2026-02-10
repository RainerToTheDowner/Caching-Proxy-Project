import requests
import time
import os
import hashlib

ttl = 60

headers = {
    "User-Agent": "RidRodLearningCache/1.0 (learning project)"
}
def cache_page(url):
    key = hashlib.sha256(url.encode()).hexdigest()
    path = f"{key}.html"

    if os.path.isfile(path):
        last_modified = os.path.getmtime(path)
        age = time.time() - last_modified
        if age < ttl:
            with open(path, "r", encoding="utf-8") as f:
                print("CACHE HIT")
                return f.read()
        else:
            print("CACHE EXPIRED")
    else:
        print("CACHE MISSED")

    print(f"Downloading {url}")
    html = requests.get(f"https://{url}", headers=headers).text
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
        print(f"Saved {path}")
    return html
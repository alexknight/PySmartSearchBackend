import os
import threading
import urllib

import requests

from utils.http import request
# from utils.logger import logger

# Global Variables
all_sites = []
lock = threading.Lock()

def fetch_top_sites_from_api(query):
    global all_sites

    # Define a list of fetch functions
    fetch_functions = [fetch_google_results]  # Add other fetch functions as needed

    threads = []

    # Start all threads
    for fetch_function in fetch_functions:
        thread = threading.Thread(target=fetch_function, args=(query,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Remove duplicates and return top 5
    all_sites = remove_duplicates(all_sites)
    return all_sites[:5], None


def remove_duplicates(elements):
    return list(dict.fromkeys(elements))


def fetch_google_results(query):
    global all_sites
    endpoint = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": os.environ["google_api_key"],
        "cx": os.environ["google_cx"],
        "q": query
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        google_data = response.json()
        sites = [item['link'] for item in google_data.get('items', [])]
        with lock:
            all_sites.extend(sites)

def fetch_bing_results(query, api_key):
    pass


def fetch_google_result_by_serp(query):
    import requests
    url = "https://serpapi.com/search?engine=google&q={}&api_key={}".format(query, os.getenv("serp_api_key"))

    payload = 'engine=google&q=Coffee&api_key={}'.format(os.getenv("serp_api_key"))
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

if __name__ == '__main__':
    # 假设你已经定义了query和api_key
    query = "example"
    api_key = "your_api_key"

    top_sites = fetch_top_sites_from_api(query)
    print(top_sites)

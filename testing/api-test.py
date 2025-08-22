import requests
import xml.etree.ElementTree as ET
import json
import sys
import time

TIMEOUT = 60
def test():
    process_time = 0
    start_time = time.time()
    url = ('https://example.com/api/xml')
    try:
        response = requests.get(url, timeout=TIMEOUT, verify=False)
        if response.status_code == 200:
            print("Response from URL (XML):")
            root = ET.fromstring(response.text)
            ET.dump(root)
            process_time = time.time() - start_time
            print("Load balancer url ---took %s seconds ---" % process_time)
        else:
            print(f"Error: Received a {response.status_code} status code.")
    except Exception as e:
        print("Time out on loading page! Perhaps server is down?")

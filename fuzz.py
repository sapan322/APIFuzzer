import time
import requests
import sys


def loop():
    for word in sys.stdin:
        response = requests.get(url=f"https://jsonplaceholder.typicode.com/{word.strip()}")
        if response.status_code != 404:
            print(f"'{response.status_code}' response code from https://jsonplaceholder.typicode.com/{word.strip()}")


print("Simple fuzzer made by sapan322")
print("Program will start in 3 sec...")
time.sleep(3)
loop()

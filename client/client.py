import requests
import multiprocessing
from datetime import datetime

# URL = "http://127.0.0.1:8000/random_reply/"
URL = "http://127.0.0.1:8085/"

def call():

    while True:
        start_time = datetime.now()
        response = requests.get(URL)
        end_time = datetime.now()
        print(end_time - start_time)

if __name__ == "__main__":

    for i in range(64):
        p = multiprocessing.Process(target=call)
        p.start()
    p.join()
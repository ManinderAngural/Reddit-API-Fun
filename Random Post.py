import datetime
import json
import random
import requests
import time


def meme(sub: str = None):
    sub = str(input("What's the name of the sub?\n"))
    start = datetime.datetime.now()
    print("\nConnecting...\n")
    url = f'https://www.reddit.com/r/{sub}/top.json?sort=top&t=week&limit=100'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/41.0.2228.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("Failed D:")
        time.sleep(3)
        exit()

    print("Connected!\n")
    response = r.json()
    i = random.randint(0, 99)
    print(f'Selected Post: {i}\n')
    title = response['data']['children'][i]['data']['title']
    source = response['data']['children'][i]['data']['url']
    if source.__contains__("v.redd.it") or source.__contains__("gifv") or source.__contains__("gfycat") \
            or not source.__contains__(""):
        print(f"{title}\n{source}")
    else:
        print(title, source, sep=" - ")
    end = datetime.datetime.now()
    total_time = (end - start).total_seconds()
    print(f"\nTotal time taken = {total_time}")

    input("Exit?")


if __name__ == '__main__':
    meme()
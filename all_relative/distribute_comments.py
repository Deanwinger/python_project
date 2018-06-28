import requests
import os



def get_url():
    r = requests.get('https://pdos.csail.mit.edu/6.824/labs/lab-1.html')
    print(r.status_code)
    print(r.text)
    # print(r.json())


if __name__ == "__main__":
     get_url()

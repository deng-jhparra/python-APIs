import requests
import json

if __name__ == "__main__":
    url = "http://httpbin.org/post"
    payload = {'nombre':'Jesus','curso':'python','nivel':'intermedio'}
    response = requests.post(url,data = json.dumps(payload))
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print (content)  

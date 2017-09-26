import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'Jesus', 'curso': 'phyton', 'nivel': 'intermedio'}
    headers = {'Content-Type': 'application/json', 'access-token': '123456'}

    responses = requests.post(url, data = json.dumps(payload), headers = headers)

    print(responses.url)

    if responses.status_code == 200:
        print(responses.content)

        print ('Leyendo encabezado')
        headers_responses = responses.headers
        server = headers_responses['server']
        print(server)

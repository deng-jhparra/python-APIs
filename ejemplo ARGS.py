import requests

if __name__ == "__main__":
    url = "http://httpbin.org/get"
    args = {'nombre':'Jesus','curso':'python','nivel':'intermedio'}
    response = requests.get(url,params=args)

if response.status_code == 200:
        contenido = response.content
        print(contenido)

import requests

if __name__ == '__main__':
    url = 'http://i.imgur.com/n9z3sLg.jpg'

    response = requests.get(url,stream = True)
    with open('imagen.jpg','wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    response.close()

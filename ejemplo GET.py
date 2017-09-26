import requests

if __name__ == '__main__':
    url = 'https://www.google.co.ve'
    response = requests.get(url)
    
    if response.status_code == 200:
        contenido = response.content
        archivo = open('google.html','wb')
        archivo.write(contenido)
        archivo.close()
        print(contenido)

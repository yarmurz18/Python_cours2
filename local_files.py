import requests

url = "https://andersonobserver.squarespace.com/storage/spring.jpg?__SQUARESPACE_CACHEVERSION=1616254525325"

response = requests.get(url)

with open('spring.jpeg', mode='wb') as file:
    content = response.content
    content += b'23235656 Vasja'
    file.write(content)

with open('spring.jpeg', mode='rb') as f:
    print(f.read())
pass








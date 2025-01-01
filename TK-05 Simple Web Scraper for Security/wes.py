import requests
from bs4 import BeautifulSoup
url="https://psr.edu.in/"
data=requests.get(url)
soup=BeautifulSoup(data.content,'html.parser')
print(soup.prettify())
with open('psr.html','w',encoding='utf=8')as file:
    file.write(soup.prettify())
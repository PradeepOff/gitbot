import requests
from bs4 import BeautifulSoup


#requesting main page of Gitam official website
main_page = requests.get('https://gitam.edu/')
#acquiring content
html_page = main_page.content
#gitving content and parsing using parser
soup = BeautifulSoup(html_page, 'html.parser')
#finding links
links = soup.find_all("a", attrs={'href': re.compile("^https://")})
#Initializing lists to store links
link_label=[]
link=[]
for t in links:
    i=t.find('href')
    link_label.append(t.string)
    #Adding links to link list
    link.append(t.get('href'))

for lin in link,link_label:
    print(lin)

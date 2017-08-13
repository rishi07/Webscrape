import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

myurl='https://www.codechef.com/contests'

uclient=ureq(myurl)
page_html=uclient.read();
uclient.close()

ps=soup(page_html,"html.parser")
c=ps.tbody
container=c.findAll("tr")

text_file=open("contests.txt","w")


print(len(container))

for i in container:
	k=i.findAll("td")
	for j in k:
		text_file.write(str(j.text)+'\n')
	text_file.write('\n')
text_file.close()



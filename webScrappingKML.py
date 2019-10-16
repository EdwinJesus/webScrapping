from bs4 import BeautifulSoup
import requests


page = requests.get("http://www.heraldo.com.mx/distrito-federal/benito-juarez/")

soup = BeautifulSoup(page.content,"html.parser")

listaUrls = []
listaNames = []
i = 0
for link in soup.find_all('a'):
    #print(link.get("href"))
    href = link.get("href")
    splitHref = href.split("/")
    if len(splitHref) > 5 :
        #print(href)
        listaUrls.append("https://www.heraldo.com.mx/v2/cache/kml/" + splitHref[3] + "_" + splitHref[4] + ".kml")
        listaNames.append(splitHref[3] + "_" + splitHref[4] + ".kml")
        #i = i + 1
        #print("https://www.heraldo.com.mx/v2/cache/kml/"+splitHref[3] +"_"+ splitHref[4]+".kml")

print("Begin download")
i = 0
for url in listaUrls:
    #if i > 4:
    #    break
    
    #print(url)
    try:
        r = requests.get(url)
        nameFile =r'''C:\BackUpKML\ ''' + listaNames[i]
        print(nameFile)
        with open(nameFile,'wb') as f:
            f.write(r.content)
    except: 
        print("No found " + url)

    i = i + 1

print("End download")

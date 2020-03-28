import time
import requests
from bs4 import BeautifulSoup
import smtplib
i=0

htmlPageUrl='https://www.worldometers.info/coronavirus/'
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
htmlPageCode= requests.get(htmlPageUrl,headers=headers)
soup = BeautifulSoup(htmlPageCode.content, 'html.parser')
convertor=soup.findAll("span",{"style":"color:#aaa"})
text=convertor[0].text
text.replace(' ', '')
strochka=text.replace(' ', '')
index=(text.find(","))
text = text[:index] + text[index+1:]
go=int(text)
print("older",go)

enterMail=input("Enter mail for statistic: ")

def sendmile(strochka,enterMail):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("screenmailserver@gmail.com","Prite21062009")

    subject="Coronavirus || Statistic"
    body="In the world coronavirus infected: "+strochka
    message= f'subject: {subject}\n\n{body}'

    server.sendmail("screenmailserver@gmail.com","prytexy@gmail.com",message)

    server.quit()

def cheker(i,text,convertor,go,enterMail):
    time.sleep(5)
    text=convertor[0].text
    htmlPageCode= requests.get(htmlPageUrl,headers=headers)
    soup = BeautifulSoup(htmlPageCode.content, 'html.parser')
    convertor=soup.findAll("span",{"style":"color:#aaa"})
    
    text.replace(' ', '')
    strochka=str(text.replace(' ', ''))
    index=(text.find(","))

    text = int(text[:index] + text[index+1:])
    if text>go:
        print("CRAZZZY!")
        go=text
        sendmile(strochka,enterMail)
    print("В мире COVID-19 заражено:",strochka)
    text=""
    cheker(i,text,convertor,go,enterMail)
    
cheker(i,text,convertor,go,enterMail)
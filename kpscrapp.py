from bs4 import BeautifulSoup
import requests
import csv
from tkinter import *
import tkinter
import os


def click():
    urls = ['https://www.kupujemprodajem.com/search.php?action=list&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=olympus%20mju%20II',
            'https://www.kupujemprodajem.com/search.php?action=list&data%5Bpage%5D=1&data%5Bprev_keywords%5D=olympus%20mju%20II&data%5Border%5D=relevance&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=canon%20ae-1',
            'https://www.kupujemprodajem.com/search.php?action=list&data%5Bpage%5D=1&data%5Bprev_keywords%5D=canon%20ae-1&data%5Border%5D=relevance&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=canon%20af35m',
            'https://www.kupujemprodajem.com/search.php?action=list&data%5Bpage%5D=1&data%5Bprev_keywords%5D=ricoh%20&data%5Border%5D=relevance&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=ricoh%20ff-70',
            'https://www.kupujemprodajem.com/search.php?action=list&submit%5Bsearch%5D=Tra%C5%BEi&dummy=name&data%5Bkeywords%5D=yashica']
    with open("kpfoto.csv", "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        header = ("Fotoaparat", "Cena")
        csvWriter.writerow(header)
        for url in urls:
            source = requests.get(url).text
            soup = BeautifulSoup(source, 'lxml')

            ad_cont = soup.findAll("div", {"class": "item clearfix"})

            for ads in ad_cont:
                adName_cont = ads.findAll("a", {"class": "adName"})
                adName = adName_cont[0].text.strip()

                adPrice_cont = ads.findAll("span", {"class": "adPrice"})
                adPrice = adPrice_cont[0].text.strip()

                table_list = (adName, adPrice)
                csvWriter.writerow(table_list)

    csvFile.close()
    os.startfile('C:\\Users\\hailehalassie\\PycharmProjects\\kpscrapp\\kpfoto.csv')

top = Tk()
L1 = Label(top, text="Kupujem Prodajem Fotoaparati",).grid(row=0,column=1)
B = Button(top, text="Generate", command= click).grid(row=1,column=1)

top.mainloop()


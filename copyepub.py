import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin


article_list=['钱学森之问','邢志恒之死','为讲座松绑']

cate=["society","wenge","society"]

book = epub.read_epub("books/1999-2010.epub")
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

text=open("index1999-2010.txt").readlines()

itembegin=2


itemnum,Name,Magnum=[],[],[]

for i in range(0,len(text)):
    for j in article_list:
        if text[i].find(j)>=0:
            tmp1=text[i].split()[0]
            year=tmp1.split("年第")[0]
            mth=tmp1.split("年第")[1].split("期")[0]
            if len(mth)==1:
                mth="0"+mth
            name=text[i].split()[1]
            prefix=year+mth
            if name.find('“')>=0:
               name=name.replace('“',"")
            if name.find('”')>=0:
               name=name.replace('”',"")
            if name.find('：')>=0:
               name=name.replace('：',"")
            if name.find('·')>=0:
               name=name.split('·')[0]
            itemnum.append(i+2)
            Name.append(name)
            Magnum.append(prefix)


def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), "html.parser")
    text = [para.get_text() for para in soup.find_all()]
    return " ".join(text)+" \n"

texts={}

Latexname=[]
for i,name in enumerate(itemnum):
    latexname="latex/%s-%s"%(Magnum[i],Name[i])
    testfile=open(latexname+".txt","w")
    texts[items[name].get_name()] = chapter_to_str(items[name])
    testfile.write(texts[items[name].get_name()])
    testfile.close()
    Latexname.append(latexname)



        

def txtfile(filename):
    template=open("template.html").readlines()
    for i in range(0,len(template)):
        if template[i].find("content begins")>=0:
           linebegin=i
        if template[i].find("content ends")>=0:
           lineend=i    
    text=open(filename+".txt").readlines()
    titleline=text[1]
    titleline=titleline.replace("\n","")
    for i in article_list:
        if titleline.find(i)>=0:
           index=article_list.index(i)
    category=cate[index]   
    for i in range(3,len(text)):
        if text[i].find(titleline)>=0:
           endline=i
           break
    magnum=titleline.split()[0]
    title=titleline.split()[1].split("·")[0]
    author=titleline.split("·")[1]
    authorpy=pinyin.get(author,format="strip")
    if authorpy.find(" ")>=0:
       authorpy=authorpy.replace(" ","")
    year=titleline.split("年第")[0]
    mth=titleline.split("年第")[1].split("期")[0]
    if len(mth)==1:
        mth="0"+mth
    prefix=year+mth
    texfile=open("latex/%s-%s%s.html"%(category,prefix,authorpy),"w")
    print(magnum,title,author)
    for i in range(0,linebegin+1):
        if template[i].find("TITLE")>=0:
           template[i]=template[i].replace("TITLE",title)
        if template[i].find("MAGAZINENUM")>=0:
           template[i]=template[i].replace("MAGAZINENUM",magnum)
        if template[i].find("AUTHOR")>=0:
           template[i]=template[i].replace("AUTHOR",author)
        texfile.write(template[i])
    for i in range(2,endline):
        texfile.write(text[i].replace("\n","</br></br>\n\n"))
    for i in range(lineend,len(template)):
        texfile.write(template[i])
    texfile.close()

#    print(magnum,title,author)
    


for i in Latexname:
    txtfile(i)
    
"""    
template=open("template.html").readlines()
for i in range(0,
"""
               

    

###write index begins
"""


itemlist=[]

for i in range(2,len(items)):
    itemlist.append(items[i])

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), "html.parser")
#    text = [para.get_text() for para in soup.find_all("p")]
    text = [para.get_text() for para in soup.find_all()]
    return " ".join(text)+" \n"
texts = {}


#testfile=open("testfile.txt","w")
test={}

indexfile=open("index1999-2010.txt","w")

def firstline():
    check=open("testfile.txt").readlines()
    indexfile.write(check[1])
    
for c in itemlist:
    testfile=open("testfile.txt","w")
    texts[c.get_name()] = chapter_to_str(c)
    testfile.write(texts[c.get_name()])
    testfile.close()
    firstline()
     
testfile.close()
indexfile.close()


"""
###write index ends

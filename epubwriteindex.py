import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin



book = epub.read_epub("books/1999-2010.epub")
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
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

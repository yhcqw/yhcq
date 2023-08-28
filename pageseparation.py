import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin


indexfile=open("index.html").readlines()
#template=open("template.html").readlines()


cat=["wenge","mao","society","people","foreignhistory","mis","discussion"]


for i in range(0,len(indexfile)):
    if indexfile[i].find("<!--------content begins--------->")>=0:
        contentbeginline=i
    if indexfile[i].find("<!--------content ends----------->")>=0:
        contentendline=i

def rewrite(category):
    newfile=open(category+".html","w")
    for i in range(0,contentbeginline+1):
        newfile.write(indexfile[i])
    beginphrase=category+"-begins"
    endphrase=category+"-ends"
    for i in range(0,len(indexfile)):
        if indexfile[i].find(beginphrase)>=0:
            beginline=i
        if indexfile[i].find(endphrase)>=0:
            endline=i
    for i in range(beginline,endline+1):
        newfile.write(indexfile[i])
    for i in range(contentendline,len(indexfile)):
        newfile.write(indexfile[i])
    newfile.close()
           

for i in cat:
    rewrite(i)

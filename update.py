#if you make any changes in template.html up to the line '<!--------content begins--------->'
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin
import shlex,subprocess

template=open("template.html").readlines()

for i in range(0,len(template)):
    if template[i].find("<!--------content begins--------->")>=0:
        linebegin=i
    

#os.system("ls *html > tmp.txt")
htmllist=open("tmp.txt").readlines()



def rewrite(filename):
    filename=filename.replace("\n","")
    oldfile=open(filename).readlines()
    phrase='<!--------content begins--------->'
    for i in range(0,len(oldfile)):
        if oldfile[i].find(phrase)>=0:
            line=i
    newfile=open(filename+"_tmp","w")
    for i in range(0,linebegin-1):
        newfile.write(template[i])
    for i in range(line,len(oldfile)):
        newfile.write(oldfile[i]) 
    newfile.close()
    os.system("mv %s %s"%(filename+"_tmp",filename))
            

for i in htmllist:
    print(i)
    rewrite(i)

import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin
import shlex,subprocess



#os.system("ls *html > tmp.txt")
htmllist=open("tmp.txt").readlines()



def rewrite(filename):
    filename=filename.replace("\n","")
    oldfile=open(filename).readlines()
    phrase='<!--------content begins--------->'
    num=221
    if oldfile[num].find(phrase)>=0:
       oldfile[num]=""
       oldfile[205]='<!--------content begins--------->\n'
       newfile=open(filename+"_tmp","w")
       for i in range(0,len(oldfile)):
           newfile.write(oldfile[i])
       newfile.close()
       os.system("mv %s %s"%(filename+"_tmp",filename))
       
            

for i in htmllist:
    print(i)
    rewrite(i)


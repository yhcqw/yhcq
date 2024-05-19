import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
import os,sys
import numpy as np
import os,sys,string
from sys import*
import pinyin
import re
import copyepub_commands


#article_list=['应该关注什么','我要说话','我的“理论工作者”经历']
#cate=["society","wenge","discussion","foreign","people","mis","mao"]

input_file="book_notes.txt"
indexfile="index1999-2010.txt"
indexhtml = "index.html"




book = epub.read_epub("books/1999-2010.epub")
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
linenum=copyepub_commands.read_until_ends(input_file)

for k in range(8,9):
   extracted_text = copyepub_commands.extract_lines(input_file, [(linenum[k], linenum[k+1]-1)])  # Extract lines 1 to 100
   maga,title,author,authorpy,cate,content = copyepub_commands.extractinfo(extracted_text)
   itemnum = None
   with open("index1999-2010.txt") as indexfile:
        for i, lines in enumerate(indexfile):
            if lines.find("期") != -1:
               title_tmp = lines.split()[1]
               index_title = copyepub_commands.clean_name(title_tmp)
               art_title =  copyepub_commands.clean_name(title)
               if index_title.find(art_title) != -1 or art_title.find(index_title) != -1:
                   itemnum= i+2

   if itemnum == None:
      print(maga+" "+title+" not found")
      exit()

   text = copyepub_commands.chapter_to_str(items[itemnum])
   print(k)
   link = copyepub_commands.txtfile(text,maga,title,author,authorpy,cate)
   print(link)
   contentb,contente,wengeb,wengee,maob,maoe,peopleb,peoplee,foreignb,foreigne,societyb,societye,misb,mise,discussionb,discussione = copyepub_commands.indexfilelines(indexhtml)
   if cate=="society":
      years = copyepub_commands.extract_years(indexhtml,societyb,societye)
   elif cate=="wenge":
      years = copyepub_commands.extract_years(indexhtml,wengeb,wengee)
   elif cate=="foreign":
      years = copyepub_commands.extract_years(indexhtml,foreignb,foreigne)
   elif cate=="mis":
      years = copyepub_commands.extract_years(indexhtml,misb,mise)
   elif cate=="mao":
      years = copyepub_commands.extract_years(indexhtml,maob,maoe)
   elif cate=="people":
      years = copyepub_commands.extract_years(indexhtml,peopleb,peoplee)

   new_content = copyepub_commands.rewritecontent(content)
   print(new_content)
